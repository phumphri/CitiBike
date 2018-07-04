-- DROP MATERIALIZED VIEW citibike.trips_by_year_minutes_gender_age;

CREATE MATERIALIZED VIEW citibike.trips_by_year_minutes_gender_age
TABLESPACE pg_default
AS
 SELECT date_part('year'::text, trips.start_time)::integer AS trip_year,
    trips.tripduration / 60 AS trip_minutes,
        CASE
            WHEN trips.gender = 1 THEN 'Male'::text
            WHEN trips.gender = 2 THEN 'Female'::text
            ELSE 'Unknown'::text
        END AS gender,
    date_part('year'::text, trips.start_time) - trips.birth_year::double precision AS age
   FROM citibike.trips
WITH NO DATA;

ALTER TABLE citibike.trips_by_year_minutes_gender_age
    OWNER TO postgres;