-- DROP MATERIALIZED VIEW citibike.user_type_by_year_month_day;

CREATE MATERIALIZED VIEW citibike.user_type_by_year_month_day
TABLESPACE pg_default
AS
 SELECT foo.trip_year,
    foo.trip_month,
    foo.trip_day,
    foo.user_type,
    count(foo.user_type) AS trips
   FROM ( SELECT date_part('year'::text, trips.start_time)::integer AS trip_year,
            date_part('month'::text, trips.start_time)::integer AS trip_month,
            date_part('day'::text, trips.start_time)::integer AS trip_day,
            trips.user_type
           FROM citibike.trips) foo
  GROUP BY foo.trip_year, foo.trip_month, foo.trip_day, foo.user_type
  ORDER BY foo.trip_year, foo.trip_month, foo.trip_day
WITH DATA;

ALTER TABLE citibike.user_type_by_year_month_day
    OWNER TO postgres;