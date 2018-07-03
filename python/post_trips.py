
import requests
import json

def run(csvpath):

    print("post_trips.run() was called.")
    res = "Boffo!"

    # Create json dictionary to hold metadata and table data.
    json_dict = {}

    # Add metadata that specifies schema and table.
    json_metadata = {}
    json_metadata["schema"] = "citibike"
    json_metadata["table"] = "trips"
    json_metadata["key"] = "start_time, bike_id"
    json_metadata["columns"] = "tripduration, start_time, stop_time, "
    json_metadata["columns"] += "start_station_id, start_station_name, start_station_latitude, start_station_longitude, "
    # json_metadata["columns"] += "stop_station_id, stop_station_name, stop_station_latitude, stop_station_longitude, "
    json_metadata["columns"] += "bike_id, "
    json_dict['metadata'] = json_metadata

    # Create table data.
    table_data = []

    # C:\Users\Patrick\OneDrive\A\02-Homework\20-Tableau\data\201306-citibike-tripdata\201306-citibike-tripdata.csv
    # import os
    # csvpath = os.path.join('C:\\', 'citibike', '201306-citibike-tripdata.csv')
    print("\ncsvpath:")
    print(csvpath)

    import csv
    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # skip the headers
        csv_table = list(csvreader)

    table_data=[]
    
    for csv_row in csv_table:

        # Validate end_station_id
        try:
            csv_row[7] = int(csv_row[7])
        except ValueError:
            csv_row[7] = None

        # Validate stop_station_name
        if csv_row[8] == "NULL":
            csv_row[8] = None

        # Validate stop_station_latitude
        if csv_row[9] == "NULL":
            csv_row[9] = None


        # Validate end_station_longitude
        if csv_row[10] == "NULL":
            csv_row[10] = None


        if len(csv_row) == 15:

            # Validate birth_year
            try:
                csv_row[13] = int(csv_row[13])
            except ValueError:
                csv_row[13] = None

            table_data.append([
                csv_row[0],         # tripduration              integer
                csv_row[1],         # start_time                timestamp (key:1)
                csv_row[2],         # end_time                  timestamp 
                csv_row[3],         # start_station_id          integer
                csv_row[4],         # start_station_name        text
                csv_row[5],         # start_station_latitude    double precision
                csv_row[6],         # start_station_longitude   double precision
                csv_row[7],         # stop_station_id           integer
                csv_row[8],         # stop_station_name         text
                csv_row[9],         # stop_station_latitude     double precision
                csv_row[10],        # stop_station_longitude    double precision
                csv_row[11],        # bike_id                   integer (key:2)
                None,               # name_localizedValue0      text
                csv_row[12],        # user_type                 text
                csv_row[13],        # birth_year                integer
                csv_row[14]]        # gender                    integer
            ) 
        elif len(csv_row) == 16:

            # Validate birth_year.
            try:
                csv_row[14] = int(csv_row[14])
            except ValueError:
                csv_row[14] = None

            table_data.append([
                csv_row[0],         # tripduration              integer
                csv_row[1],         # start_time                timestamp (key:1)
                csv_row[2],         # end_time                timestamp 
                csv_row[3],         # start_station_id          integer
                csv_row[4],         # start_station_name        text
                csv_row[5],         # start_station_latitude    double precision
                csv_row[6],         # start_station_longitude   double precision
                csv_row[7],         # stop_station_id           integer
                csv_row[8],         # stop_station_name         text
                csv_row[9],         # stop_station_latitude     double precision
                csv_row[10],        # stop_station_longitude    double precision
                csv_row[11],        # bike_id                   integer (key:2)
                csv_row[12],        # name_localizedValue0      text
                csv_row[13],        # user_type                 text
                csv_row[14],        # birth_year                integer
                csv_row[15]]        # gender                    integer
            )
        else:
            print("Unexpected row length:", len(csv_row))


    # Add table_data to json dictionary.
    json_dict['table_data'] = table_data

    json_string = json.dumps(json_dict)


    # url = 'https://its-a-gas.herokuapp.com/domesticautos'  # Using app.py on Heroku, Postgres on AWS.
    url = 'http://127.0.0.1:5000/trips'            # Using app.py and Postgres locally.

    print("Calling requests.post(url, json_string).")

    res = requests.post(url, json=json_string)

    if res is None:
        print("res was null.")
    else:
        print("res.ok:", res.ok)
        print("res.status_code:", res.status_code)
        print("res.reason:", res.reason)
        print("res.text:", res.text)

    return res

# run()



