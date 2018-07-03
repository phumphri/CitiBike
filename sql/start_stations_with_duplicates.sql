-- DROP MATERIALIZED VIEW citibike.start_stations_with_duplicates;

CREATE MATERIALIZED VIEW citibike.start_stations_with_duplicates
TABLESPACE pg_default
AS
 SELECT trips.start_station_id,
    trips.start_station_name,
    trips.start_station_latitude,
    trips.start_station_longitude,
    count(*)::integer AS trips
   FROM citibike.trips
  WHERE (trips.start_station_id IN ( SELECT foo.start_station_id
           FROM ( SELECT trips_1.start_station_id,
                    count(trips_1.start_station_id)::integer AS trips
                   FROM citibike.trips trips_1
                  GROUP BY trips_1.start_station_id
                  ORDER BY (count(trips_1.start_station_id)) DESC
                 LIMIT 10) foo))
  GROUP BY trips.start_station_id, trips.start_station_name, trips.start_station_latitude, trips.start_station_longitude
WITH DATA;

ALTER TABLE citibike.start_stations_with_duplicates
    OWNER TO postgres;