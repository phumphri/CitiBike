
-- DROP MATERIALIZED VIEW citibike.trips_by_year_month;

CREATE MATERIALIZED VIEW citibike.trips_by_year_month_day
TABLESPACE pg_default
AS
 SELECT foo.trip_year,
    foo.trip_month,
    foo.trip_day,
    count(*)::integer AS trips
   FROM ( SELECT 
		 	extract(year from trips.start_time)::integer AS trip_year,
            extract(month from trips.start_time)::integer AS trip_month,
            extract(day from trips.start_time)::integer AS trip_day
           FROM citibike.trips) foo
  GROUP BY foo.trip_year, foo.trip_month, foo.trip_day
  ORDER BY foo.trip_year, foo.trip_month, foo.trip_day
WITH DATA;

ALTER TABLE citibike.trips_by_year_month
    OWNER TO postgres;