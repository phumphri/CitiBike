-- View: citibike.start_stations

-- DROP VIEW citibike.start_stations;

CREATE OR REPLACE VIEW citibike.start_stations AS
 SELECT DISTINCT start_stations_with_duplicates.start_station_id,
    first_value(start_stations_with_duplicates.start_station_name) OVER (PARTITION BY start_stations_with_duplicates.start_station_id) AS start_station_name,
    first_value(start_stations_with_duplicates.start_station_latitude) OVER (PARTITION BY start_stations_with_duplicates.start_station_id) AS start_station_latitude,
    first_value(start_stations_with_duplicates.start_station_longitude) OVER (PARTITION BY start_stations_with_duplicates.start_station_id) AS start_station_longitude,
    sum(start_stations_with_duplicates.trips) OVER (PARTITION BY start_stations_with_duplicates.start_station_id)::integer AS trips
   FROM citibike.start_stations_with_duplicates
  ORDER BY start_stations_with_duplicates.start_station_id;

ALTER TABLE citibike.start_stations
    OWNER TO postgres;

