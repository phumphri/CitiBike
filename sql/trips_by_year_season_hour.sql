-- DROP MATERIALIZED VIEW public.trips_by_year_season_hour;

CREATE MATERIALIZED VIEW citibike.trips_by_year_season_hour
TABLESPACE pg_default
AS
 SELECT foo.trip_year,
    foo.season,
    foo.trip_hour,
    count(foo.trip_hour)::integer AS trips
   FROM ( SELECT date_part('year'::text, trips.start_time)::integer AS trip_year,
            'Summer'::text AS season,
            date_part('hour'::text, trips.start_time)::integer AS trip_hour
           FROM citibike.trips
          WHERE date_part('month'::text, trips.start_time) = ANY (ARRAY['6'::double precision, '7'::double precision, '8'::double precision])
        UNION ALL
         SELECT date_part('year'::text, trips.start_time)::integer AS trip_year,
            'Winter'::text AS season,
            date_part('hour'::text, trips.start_time)::integer AS trip_hour
           FROM citibike.trips
          WHERE date_part('month'::text, trips.start_time) = ANY (ARRAY['12'::double precision, '1'::double precision, '2'::double precision])) foo
  GROUP BY foo.trip_year, foo.season, foo.trip_hour
  ORDER BY foo.trip_year, foo.trip_hour, foo.season
WITH NO DATA;

ALTER TABLE citibike.trips_by_year_season_hour
    OWNER TO postgres;