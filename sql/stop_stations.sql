CREATE OR REPLACE VIEW citibike.stop_stations AS
 SELECT DISTINCT stop_stations_with_duplicates.stop_station_id,
    first_value(stop_stations_with_duplicates.stop_station_name) OVER (PARTITION BY stop_stations_with_duplicates.stop_station_id) AS stop_station_name,
    first_value(stop_stations_with_duplicates.stop_station_latitude) OVER (PARTITION BY stop_stations_with_duplicates.stop_station_id) AS stop_station_latitude,
    first_value(stop_stations_with_duplicates.stop_station_longitude) OVER (PARTITION BY stop_stations_with_duplicates.stop_station_id) AS stop_station_longitude,
    sum(stop_stations_with_duplicates.trips) OVER (PARTITION BY stop_stations_with_duplicates.stop_station_id)::integer AS trips
   FROM citibike.stop_stations_with_duplicates
  ORDER BY stop_stations_with_duplicates.stop_station_id;

ALTER TABLE citibike.stop_stations
    OWNER TO postgres;

