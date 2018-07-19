"""
Version 2018 07 19 09 48
"""

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


# Assigning the Flask framework.
app = Flask(__name__)
CORS(app)

def connect_to_postgres():
    hostname = socket.gethostname()
    print("socket.hostname():", hostname)
    print("os.environ['LOCAL_POSTGRES]:", os.environ['LOCAL_POSTGRES'])
    try:
        if (hostname == 'XPS'):
            conn = psycopg2.connect(os.environ['LOCAL_POSTGRES'])
            print('Connection okay.')
            return conn
        elif (hostname == 'DESKTOP-S08TN4O'):  
            conn = psycopg2.connect(os.environ['LOCAL_POSTGRES'])
            print('Connection okay.')
            return conn
        else:
            conn = psycopg2.connect(os.environ['AWS_POSTGRES'])
            print('Connection okay.')
            return conn
    except Exception as e:
        print('Connection failed:', e)


@app.route('/$metadata', methods=['GET'])
def metadata():  # pragma: no cover
    with open('metadata.xml', 'r') as metadata_file:
        content = metadata_file.read()
        return Response(content, mimetype="text/xml")


@app.route('/trips_by_year_month', methods=['GET'])
def trips_by_year_month():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from citibike.trips_by_year_month order by trip_year, trip_month"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            table_data = cur.fetchall()
            print("Fetch All Okay")

            # forecast code start

            df = pd.DataFrame(table_data, columns=['Trip Year', 'Trip Month', 'Trip Month Name', 'Trips'])
            
            X = df[['Trip Year', 'Trip Month']]
            print(X)

            y = df[['Trips']]
            print(y)



            # forecast code end




            value_list = []

            for table_entry_list in table_data:
                table_entry_json = {}
                table_entry_json["trip_year"] = table_entry_list[0]
                table_entry_json["trip_month"] = table_entry_list[1]
                table_entry_json["trip_month_name"] = table_entry_list[2]
                table_entry_json["trips"] = table_entry_list[3]
                value_list.append(table_entry_json)
            
            # Create json dictionary to hold metadata and table data.
            json_dict = {}
            json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#trips_by_year_month"


            # Add table_data to json dictionary.
            json_dict["value"] = value_list

            json_object = jsonify(json_dict)
            print("jsonify Okay")
            print(json_object)

            # Experiment
            # response = json.dumps(json_object)
            # print(type(json.dumps(json_dict)))
            # response = Response(json.dumps(json_object))

            response = json_object
            response.headers['Content-Type'] = "application/json; odata.metadata=minimal"
            response.headers['OData-Version'] = "4.0"
            response.headers['Cache-Control'] = "no-cache"
            response.headers['Pragma'] = "no-cache"
            response.headers['Vary'] = "Accept-Encoding"
            response.headers['Expires'] = "-1"

            return response

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close















@app.route('/age_minutes_by_year_month_day', methods=['GET'])
def age_minutes_by_year_month_day():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from citibike.age_minutes_by_year_month_day"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            table_data = cur.fetchall()
            print("Fetch All Okay")

            value_list = []


            for table_entry_list in table_data:
                table_entry_json = {}
                table_entry_json["trip_year"] = table_entry_list[0]
                table_entry_json["trip_month"] = table_entry_list[1]
                table_entry_json["trip_day"] = table_entry_list[2]
                table_entry_json["age"] = table_entry_list[3]
                table_entry_json["trip_minutes"] = table_entry_list[4]
                value_list.append(table_entry_json)
            
            # Create json dictionary to hold metadata and table data.
            json_dict = {}
            json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#age_minutes_by_year_month_day"


            # Add table_data to json dictionary.
            json_dict["value"] = value_list

            json_object = jsonify(json_dict)
            print("jsonify Okay")
            # print(json_object)

            # Experiment
            # response = json.dumps(json_object)
            # print(type(json.dumps(json_dict)))
            # response = Response(json.dumps(json_object))

            response = json_object
            response.headers['Content-Type'] = "application/json; odata.metadata=minimal"
            response.headers['OData-Version'] = "4.0"
            response.headers['Cache-Control'] = "no-cache"
            response.headers['Pragma'] = "no-cache"
            response.headers['Vary'] = "Accept-Encoding"
            response.headers['Expires'] = "-1"

            return response

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 

@app.route('/gender_trips_by_year_month_day', methods=['GET'])
def gender_trips_by_year_month_day():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from citibike.gender_trips_by_year_month_day"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            table_data = cur.fetchall()
            print("Fetch All Okay")

            value_list = []


            for table_entry_list in table_data:
                table_entry_json = {}
                table_entry_json["trip_year"] = table_entry_list[0]
                table_entry_json["trip_month"] = table_entry_list[1]
                table_entry_json["trip_day"] = table_entry_list[2]
                table_entry_json["gender"] = table_entry_list[3]
                table_entry_json["trips"] = table_entry_list[4]
                value_list.append(table_entry_json)
            
            # Create json dictionary to hold metadata and table data.
            json_dict = {}
            json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#gender_trips_by_year_month_day"


            # Add table_data to json dictionary.
            json_dict["value"] = value_list

            json_object = jsonify(json_dict)
            print("jsonify Okay")
            print(json_object)

            # Experiment
            # response = json.dumps(json_object)
            # print(type(json.dumps(json_dict)))
            # response = Response(json.dumps(json_object))

            response = json_object
            response.headers['Content-Type'] = "application/json; odata.metadata=minimal"
            response.headers['OData-Version'] = "4.0"
            response.headers['Cache-Control'] = "no-cache"
            response.headers['Pragma'] = "no-cache"
            response.headers['Vary'] = "Accept-Encoding"
            response.headers['Expires'] = "-1"

            return response

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 



@app.route('/stop_stations', methods=['GET'])
def stop_stations():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from citibike.stop_stations"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            table_data = cur.fetchall()
            print("Fetch All Okay")

            value_list = []


            for table_entry_list in table_data:
                table_entry_json = {}
                table_entry_json["stop_station_id"] = table_entry_list[0]
                table_entry_json["stop_station_name"] = table_entry_list[1]
                table_entry_json["stop_station_latitude"] = table_entry_list[2]
                table_entry_json["stop_station_longitude"] = table_entry_list[3]
                table_entry_json["trips"] = table_entry_list[4]
                value_list.append(table_entry_json)
            
            # Create json dictionary to hold metadata and table data.
            json_dict = {}
            json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#stop_stations"


            # Add table_data to json dictionary.
            json_dict["value"] = value_list

            json_object = jsonify(json_dict)
            print("jsonify Okay")
            print(json_object)

            # Experiment
            # response = json.dumps(json_object)
            # print(type(json.dumps(json_dict)))
            # response = Response(json.dumps(json_object))

            response = json_object
            response.headers['Content-Type'] = "application/json; odata.metadata=minimal"
            response.headers['OData-Version'] = "4.0"
            response.headers['Cache-Control'] = "no-cache"
            response.headers['Pragma'] = "no-cache"
            response.headers['Vary'] = "Accept-Encoding"
            response.headers['Expires'] = "-1"

            return response

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close



@app.route('/start_stations', methods=['GET'])
def start_stations():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from citibike.start_stations"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            table_data = cur.fetchall()
            print("Fetch All Okay")

            value_list = []


            for table_entry_list in table_data:
                table_entry_json = {}
                table_entry_json["start_station_id"] = table_entry_list[0]
                table_entry_json["start_station_name"] = table_entry_list[1]
                table_entry_json["start_station_latitude"] = table_entry_list[2]
                table_entry_json["start_station_longitude"] = table_entry_list[3]
                table_entry_json["trips"] = table_entry_list[4]
                value_list.append(table_entry_json)
            
            # Create json dictionary to hold metadata and table data.
            json_dict = {}
            json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#start_stations"


            # Add table_data to json dictionary.
            json_dict["value"] = value_list

            json_object = jsonify(json_dict)
            print("jsonify Okay")
            print(json_object)

            # Experiment
            # response = json.dumps(json_object)
            # print(type(json.dumps(json_dict)))
            # response = Response(json.dumps(json_object))

            response = json_object
            response.headers['Content-Type'] = "application/json; odata.metadata=minimal"
            response.headers['OData-Version'] = "4.0"
            response.headers['Cache-Control'] = "no-cache"
            response.headers['Pragma'] = "no-cache"
            response.headers['Vary'] = "Accept-Encoding"
            response.headers['Expires'] = "-1"

            return response

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close




@app.route('/trips_by_year_season_hour', methods=['GET'])
def trips_by_year_season_hour():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from citibike.trips_by_year_season_hour"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            table_data = cur.fetchall()
            print("Fetch All Okay")

            value_list = []


            for table_entry_list in table_data:
                table_entry_json = {}
                table_entry_json["trip_year"] = table_entry_list[0]
                table_entry_json["season"] = table_entry_list[1]
                table_entry_json["trip_hour"] = table_entry_list[2]
                table_entry_json["trips"] = table_entry_list[3]
                value_list.append(table_entry_json)
            
            # Create json dictionary to hold metadata and table data.
            json_dict = {}
            json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#trips_by_year_season_hour"


            # Add table_data to json dictionary.
            json_dict["value"] = value_list

            json_object = jsonify(json_dict)
            print("jsonify Okay")
            print(json_object)

            # Experiment
            # response = json.dumps(json_object)
            # print(type(json.dumps(json_dict)))
            # response = Response(json.dumps(json_object))

            response = json_object
            response.headers['Content-Type'] = "application/json; odata.metadata=minimal"
            response.headers['OData-Version'] = "4.0"
            response.headers['Cache-Control'] = "no-cache"
            response.headers['Pragma'] = "no-cache"
            response.headers['Vary'] = "Accept-Encoding"
            response.headers['Expires'] = "-1"

            return response

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close



@app.route('/user_types_by_year_month_day', methods=['GET'])
def user_types_by_year_month_day():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from citibike.user_type_by_year_month_day_percentage"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            table_data = cur.fetchall()
            print("Fetch All Okay")

            value_list = []


            for table_entry_list in table_data:
                table_entry_json = {}
                table_entry_json["trip_year"] = table_entry_list[0]
                table_entry_json["trip_month"] = table_entry_list[1]
                table_entry_json["trip_day"] = table_entry_list[2]
                table_entry_json["user_type"] = table_entry_list[3]
                table_entry_json["trips"] = table_entry_list[4]
                table_entry_json["percentage"] = table_entry_list[5]
                value_list.append(table_entry_json)
            
            # Create json dictionary to hold metadata and table data.
            json_dict = {}
            json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#user_types_by_year_month_day"


            # Add table_data to json dictionary.
            json_dict["value"] = value_list

            json_object = jsonify(json_dict)
            print("jsonify Okay")
            print(json_object)

            # Experiment
            # response = json.dumps(json_object)
            # print(type(json.dumps(json_dict)))
            # response = Response(json.dumps(json_object))

            response = json_object
            response.headers['Content-Type'] = "application/json; odata.metadata=minimal"
            response.headers['OData-Version'] = "4.0"
            response.headers['Cache-Control'] = "no-cache"
            response.headers['Pragma'] = "no-cache"
            response.headers['Vary'] = "Accept-Encoding"
            response.headers['Expires'] = "-1"

            return response

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close




@app.route('/trips_by_year_month_day', methods=['GET'])
def trips_by_year_month_day():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from citibike.trips_by_year_month_day"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            table_data = cur.fetchall()
            print("Fetch All Okay")

            value_list = []


            for table_entry_list in table_data:
                table_entry_json = {}
                table_entry_json["trip_year"] = table_entry_list[0]
                table_entry_json["trip_month"] = table_entry_list[1]
                table_entry_json["trip_day"] = table_entry_list[2]
                table_entry_json["trips"] = table_entry_list[3]
                value_list.append(table_entry_json)
            
            # Create json dictionary to hold metadata and table data.
            json_dict = {}
            json_dict["odata.metadata"] = "http://127.0.0.1:5000/$metadata#trips_by_year_month_day"


            # Add table_data to json dictionary.
            json_dict["value"] = value_list

            json_object = jsonify(json_dict)
            print("jsonify Okay")
            print(json_object)

            # Experiment
            # response = json.dumps(json_object)
            # print(type(json.dumps(json_dict)))
            # response = Response(json.dumps(json_object))

            response = json_object
            response.headers['Content-Type'] = "application/json; odata.metadata=minimal"
            response.headers['OData-Version'] = "4.0"
            response.headers['Cache-Control'] = "no-cache"
            response.headers['Pragma'] = "no-cache"
            response.headers['Vary'] = "Accept-Encoding"
            response.headers['Expires'] = "-1"

            return response

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close




@app.route('/trips', methods=['POST', 'GET', 'DELETE', 'PROPFIND'])
def trips():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select to_char(start_time, 'YYYY-MM-DD HH24:MI:SS'), bike_id from citibike.trips limit 10"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            table_data = cur.fetchall()
            print("Fetch All Okay")

            value_list = []

            for table_entry_list in table_data:
                table_entry_json = {}
                table_entry_json["start_time"] = table_entry_list[0]
                table_entry_json["bike_id"] = table_entry_list[1]
                value_list.append(table_entry_json)
            
            # Create json dictionary to hold metadata and table data.
            json_dict = {}

            # Add table_data to json dictionary.
            json_dict["value"] = value_list

            json_object = jsonify(json_dict)
            print("jsonify Okay")
            print(json_object)

            # Experiment
            # response = json.dumps(json_object)
            # print(type(json.dumps(json_dict)))
            # response = Response(json.dumps(json_object))

            response = json_object
            response.headers['Content-Type'] = "application/json; odata.metadata=minimal"
            response.headers['OData-Version'] = "4.0"
            response.headers['Cache-Control'] = "no-cache"
            response.headers['Pragma'] = "no-cache"
            response.headers['Vary'] = "Accept-Encoding"
            response.headers['Expires'] = "-1"

            return response

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 
    if request.method == 'POST':

        json_string = request.get_json(silent=True)

        json_dict = json.loads(json_string)

        json_metadata = json_dict['metadata']

        print("schema:", json_metadata['schema'])
        print("table:", json_metadata['table'])
    
        status_message = ""

        if json_metadata['schema'] != "citibike":
            status_message = "Inncorrect schema in metadata. "
            status_message += "Expected citibike.  "
            status_message += "Found "
            status_message += json_metadata['schema']
            status_message += "."
            return status_message

        if json_metadata['table'] != "trips":
            status_message = "Inncorrect table in metadata. "
            status_message += "Expected trips.  "
            status_message += "Found "
            status_message += json_metadata['table']
            status_message += "."
            return status_message

        sql = "insert into citibike.trips "

        sql += "values ( "

        for i in range(len(json_dict['table_data'][0]) - 1):
            sql += "%s, "
            i = i

        sql += "%s) "
            
        sql += "on conflict (" + json_metadata['key'] + ") do nothing; "

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.executemany(sql, json_dict['table_data'])
            print('Execute Many Okay.')

            status_message = cur.statusmessage
            print("cur.statusmessage:", status_message)

            conn.commit()
            print('Execute Many Commit Okay.')

        except Exception as e:
            print('Execute Many Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 
 
        return status_message        
    
    if request.method == 'DELETE':

        sql = "delete from citibike.trips"

        status_message = sql

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Delete Okay.')

            status_message = cur.statusmessage
            print("cur.statusmessage:", status_message)

            conn.commit()
            print('Delete Commit Okay.')

        except Exception as e:
            print('Execute Many Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 
        return status_message    

    if request.method == "PROPFIND":
        print("\nPROPFIND was called:")
        print(request.want_form_data_parsed)
        return("Boffo!")
    
    return "The request.method was not method POST, GET, or DELETE."



if __name__ == "__main__":
    hostname = socket.gethostname()
    print("socket.hostname():", hostname)
    
    if (hostname == 'XPS'):
        app.run(debug=True)
    elif (hostname == 'DESKTOP-S08TN4O'):  
        app.run(debug=True)
    else:
        from os import environ
        print("Port", environ.get("PORT", "Not Found"))
        app.run(debug=False, host='0.0.0.0', port=int(environ.get("PORT", 5000)))

