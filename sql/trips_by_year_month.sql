-- View: citibike.trips_by_year_month

-- DROP MATERIALIZED VIEW citibike.trips_by_year_month;

CREATE MATERIALIZED VIEW citibike.trips_by_year_month
TABLESPACE pg_default
AS
 SELECT foo.trip_year,
    foo.trip_month,
    foo.trip_month_name,
    count(*)::integer AS trips
   FROM ( SELECT date_part('year'::text, trips.start_time)::integer AS trip_year,
            date_part('month'::text, trips.start_time)::integer AS trip_month,
            to_char(trips.start_time, 'Month'::text) AS trip_month_name
           FROM citibike.trips) foo
  GROUP BY foo.trip_year, foo.trip_month, foo.trip_month_name
  ORDER BY foo.trip_year, foo.trip_month
WITH DATA;

ALTER TABLE citibike.trips_by_year_month
    OWNER TO postgres;