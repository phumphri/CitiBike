
-- DROP MATERIALIZED VIEW citibike.gender_trips_by_year_month_day;

CREATE MATERIALIZED VIEW citibike.gender_trips_by_year_month_day
TABLESPACE pg_default
AS
 SELECT foo.trip_year,
    foo.trip_month,
    foo.trip_day,
    foo.gender,
    count(*)::integer AS trips
   FROM ( SELECT date_part('year'::text, trips.start_time)::integer AS trip_year,
            date_part('month'::text, trips.start_time)::integer AS trip_month,
            date_part('day'::text, trips.start_time)::integer AS trip_day,
                CASE
                    WHEN trips.gender = 1 THEN 'Male'::text
                    WHEN trips.gender = 2 THEN 'Female'::text
                    ELSE 'Unknown'::text
                END AS gender
           FROM citibike.trips) foo
  GROUP BY foo.trip_year, foo.trip_month, foo.trip_day, foo.gender
  ORDER BY foo.trip_year, foo.trip_month, foo.trip_day, foo.gender
WITH DATA;

ALTER TABLE citibike.gender_trips_by_year_month_day
    OWNER TO postgres;