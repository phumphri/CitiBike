-- DROP MATERIALIZED VIEW citibike.start_stations_with_duplicates;

CREATE MATERIALIZED VIEW citibike.stop_stations_with_duplicates
TABLESPACE pg_default
AS
 SELECT trips.stop_station_id,
    trips.stop_station_name,
    trips.stop_station_latitude,
    trips.stop_station_longitude,
    count(*)::integer AS trips
   FROM citibike.trips
  WHERE (trips.stop_station_id IN ( SELECT foo.stop_station_id
           FROM ( SELECT trips_1.stop_station_id,
                    count(trips_1.stop_station_id)::integer AS trips
                   FROM citibike.trips trips_1
				 	where trips_1.stop_station_id is not null
                  GROUP BY trips_1.stop_station_id
                  ORDER BY (count(trips_1.stop_station_id)) DESC
                 LIMIT 10) foo))
	and trips.stop_station_name is not null
	and trips.stop_station_latitude is not null
	and trips.stop_station_longitude is not null
  GROUP BY trips.stop_station_id, trips.stop_station_name, trips.stop_station_latitude, trips.stop_station_longitude
WITH DATA;

ALTER TABLE citibike.stop_stations_with_duplicates
    OWNER TO postgres;