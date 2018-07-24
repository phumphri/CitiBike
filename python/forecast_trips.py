
from requests.models import Response
import psycopg2
import pandas as pd
import numpy as np
import math
import socket
import os
import json
import flask
from flask import (
    Response,
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_cors import CORS
import os.path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/ 
from statsmodels.tsa.seasonal import seasonal_decompose
from datetime import datetime

# Connect to local Postgres database if working from workstation or laptop.
# Otherwise connect to Postgres datase hosted by AWS/RDS.
def connect_to_postgres():
    hostname = socket.gethostname()
    print("socket.hostname():", hostname)
    try:
        if (hostname == 'XPS'):
            conn = psycopg2.connect(os.environ['LOCAL_POSTGRES'])
            print('Connection okay.', os.environ['LOCAL_POSTGRES'])
            return conn
        elif (hostname == 'DESKTOP-S08TN4O'):  
            conn = psycopg2.connect(os.environ['LOCAL_POSTGRES'])
            print('Connection okay.', os.environ['LOCAL_POSTGRES'])
            return conn
        else:
            conn = psycopg2.connect(os.environ['AWS_POSTGRES'])
            print('Connection okay.', os.environ['AWS_POSTGRES'])
            return conn
    except Exception as e:
        print('Connection failed:', e)
        

# Select current data from the database.
conn = None
conn = connect_to_postgres()
if conn is None:
    print("Database Connection Failed.")
else:
    print("Database Connection Okay.")

sql = """select 
    trip_year,
    trip_month,
    trips 
    from citibike.trips_by_year_month 
    order by trip_year, trip_month"""

try:
    cur = conn.cursor()
    print('Cursor okay.')

    cur.execute(sql)
    print('Execute Okay.')

    table_data = cur.fetchall()
    print("Fetch All Okay")

except Exception as e:
    print('Execute Failed', str(e))

finally:
    if conn is not None:
        conn.close
        print("Close Okay")


# Load selected data into a dataframe.
df = pd.DataFrame(table_data, columns=['Trip Year', 'Trip Month', 'Trips'])


# Add Trip Timestamp based on Trip Year and Trip Month.
# Trip Timestamp is needed for Tred and Seasonal decomposition.

for index, row in df.iterrows():
    ty = df.loc[index, 'Trip Year'].astype(str)
    tm = df.loc[index, 'Trip Month'].astype(str)
    wtf = ty + tm
    print('About to call pd.to_datetime.')
    df.loc[index, 'Trip Timestamp'] = pd.to_datetime(wtf, format="%Y%m")
    print('Called pd.to_datetime.')


# df['Trip Timestamp'] = pd.to_datetime(df['Trip Year'].astype(str) + df['Trip Month'].astype(str), format='%Y%m')

# df['Trip Timestamp'] = pd.Series()
# for index, row in df.iterrows():
#     df.loc[index, 'Trip Timestamp'] = datetime.strptime(df.loc[index, 'Trip Year'].astype(str) + df.loc[index, 'Trip Month'].astype(str), '%Y%m')

df1 = df.set_index('Trip Timestamp')


# Decompose the Trips data into Trend and Seasonal Series.
series = df1['Trips']
result = seasonal_decompose(series, model='multiplicative')

trend_array = result.trend.get_values()
trend_array = trend_array.astype(int)
trend_series = pd.Series(trend_array)

seasonal_array = result.seasonal.get_values()
seasonal_series = pd.Series(seasonal_array)


# Create a new dataframe from the orignal data, Trend, and Seasonal Series.
# Decomposition does not calculate the first and last six periods.
df_extended = pd.concat([df, trend_series, seasonal_series], axis=1)
df_extended = df_extended.rename(columns={0:'Trend', 1:'Seasonal'})
df_extended = df_extended[6:-6]
df_extended = df_extended.reset_index(col_level=0)
df_extended = df_extended.drop(['index'], axis=1)


# Train a model to predict a trend in Trips.
X = df_extended.index
X = np.array(X)
X = X.reshape(-1, 1)

y = np.array(df_extended['Trend'])
model = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model.fit(X_train, y_train)
model_score = model.score(X_test, y_test)


# Predict Trend for the additional months.
X_predict = range(48, 60, 1)
X_predict = np.array(X_predict)
X_predict = X_predict.reshape(-1,1)
y_predict = model.predict(X_predict)
y_predict = y_predict.astype(int)
y_predict = pd.Series(y_predict, name='Predict', index=pd.Index(range(48,60,1)))
y_predict 


# Create Dataframe Final as the concatenation of the Extended Dataframe and 
# Trend Prediction Series.
df_final = pd.concat([df_extended, y_predict], axis=1)
df_final = df_final.fillna(0)
df_final = df_final.drop(columns=['Trip Timestamp'])


# For the additional periods, set Trip Year and Trip Month.
previous_year = 0
previous_month = 0
for index, row in df_final.iterrows():
    if row['Trip Year'] == 0:
        if previous_month == 12:
            previous_year += 1
            previous_month = 1
        else:
            previous_month += 1
        df_final.loc[index,'Trip Year'] = previous_year
        df_final.loc[index, 'Trip Month'] = previous_month
    else:
        previous_year = row['Trip Year']
        previous_month = row['Trip Month']


# For the additional periods, set Seasonal factor to the Seasonal factor from 
# the previous year.
for index, row in df_final.iterrows():
    if df_final.loc[index, 'Seasonal'] == 0:
        df_final.loc[index, 'Seasonal'] = df_final.loc[index - 12, 'Seasonal']


# For additional periods, set Trend to Predict.
for index, row in df_final.iterrows():
    if row['Trend'] == 0:
        df_final.loc[index, 'Trend'] = df_final.loc[index, 'Predict']


# For additional periods, alculate Trips by multiplying Trend and Seasonl when 
# Trips is zero.
for index, row in df_final.iterrows():
    if row['Trips'] == 0:
        df_final.loc[index, 'Trips'] = df_final.loc[index, 'Trend'] * df_final.loc[index, 'Seasonal']
integer_fields = list(df_final.columns.values)
integer_fields.remove('Seasonal')
df_final[integer_fields] = df_final[integer_fields].astype(int)


# Return linear regression.
def get_linear_regression():
    value_list = []
    for index, row in df_final.iterrows():
        value_entry = {}
        value_entry['trip_year'] = int(df_final.loc[index, 'Trip Year'])
        value_entry['trip_month'] = int(df_final.loc[index, 'Trip Month'])
        value_entry['trips'] = int(df_final.loc[index, 'Trend'])
        value_list.append(value_entry)

    json_dict = {}
    json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#linear_regessions"

    # Add data to json dictionary.
    json_dict["value"] = value_list

    return(json_dict)
        
# Return seasonal factors.
def get_seasonal_factors():
    value_list = []
    for index, row in df_final.iterrows():
        value_entry = {}
        value_entry['trip_year'] = int(df_final.loc[index, 'Trip Year'])
        value_entry['trip_month'] = int(df_final.loc[index, 'Trip Month'])
        value_entry['seasonal_factor'] = float(df_final.loc[index, 'Seasonal'])
        value_list.append(value_entry)

    json_dict = {}
    json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#seasonal_factors"

    # Add data to json dictionary.
    json_dict["value"] = value_list

    return(json_dict)
        
# Return forecasts.
def get_forecasts():
    value_list = []
    for index, row in df_final.iterrows():
        value_entry = {}
        value_entry['trip_year'] = int(df_final.loc[index, 'Trip Year'])
        value_entry['trip_month'] = int(df_final.loc[index, 'Trip Month'])
        value_entry['trips'] = int(df_final.loc[index, 'Trips'])
        value_list.append(value_entry)

    json_dict = {}
    json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#forecasts"

    # Add data to json dictionary.
    json_dict["value"] = value_list

    return(json_dict)




