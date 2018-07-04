

DROP MATERIALIZED VIEW citibike.age_minutes_by_year_month_day;

CREATE MATERIALIZED VIEW citibike.age_minutes_by_year_month_day
TABLESPACE pg_default
AS
 SELECT foo.trip_year,
    foo.trip_month,
    foo.trip_day,
    foo.age,
    avg(foo.trip_minutes)::integer AS trip_minutes
   FROM ( SELECT date_part('year'::text, trips.start_time)::integer AS trip_year,
            date_part('month'::text, trips.start_time)::integer AS trip_month,
            date_part('day'::text, trips.start_time)::integer AS trip_day,
            date_part('year'::text, trips.start_time) - trips.birth_year::integer AS age,
            (trips.tripduration / 60)::integer AS trip_minutes
           FROM citibike.trips
          WHERE trips.birth_year IS NOT NULL AND trips.tripduration IS NOT NULL) foo
  WHERE foo.age < 100::integer
  GROUP BY foo.trip_year, foo.trip_month, foo.trip_day, foo.age
  ORDER BY foo.trip_year, foo.trip_month, foo.trip_day, foo.age
WITH DATA;

ALTER TABLE citibike.age_minutes_by_year_month_day
    OWNER TO postgres;