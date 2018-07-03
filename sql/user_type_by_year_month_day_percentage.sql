-- DROP VIEW citibike.user_type_by_year_month_day_percentage;

CREATE OR REPLACE VIEW citibike.user_type_by_year_month_day_percentage AS
 SELECT bar.trip_year,
    bar.trip_month,
    bar.trip_day,
    bar.user_type,
    bar.trips,
    ((bar.trips * 100)::numeric / bar.sum)::integer AS percentage
   FROM ( SELECT user_type_by_year_month_day.trip_year,
            user_type_by_year_month_day.trip_month,
            user_type_by_year_month_day.trip_day,
            user_type_by_year_month_day.user_type,
            user_type_by_year_month_day.trips,
            sum(user_type_by_year_month_day.trips) OVER (PARTITION BY user_type_by_year_month_day.trip_year, user_type_by_year_month_day.trip_month, user_type_by_year_month_day.trip_day) AS sum
           FROM citibike.user_type_by_year_month_day) bar;

ALTER TABLE citibike.user_type_by_year_month_day_percentage
    OWNER TO postgres;