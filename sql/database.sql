-- Table: citibike.trips

-- DROP TABLE citibike.trips;

CREATE TABLE citibike.trips
(
    tripduration integer,
    start_time timestamp without time zone NOT NULL,
    stop_time timestamp without time zone,
    start_station_id integer,
    start_station_name text COLLATE pg_catalog."default",
    start_station_latitude double precision,
    start_station_longitude double precision,
    stop_station_id integer,
    stop_station_name text COLLATE pg_catalog."default",
    stop_station_latitude double precision,
    stop_station_longitude double precision,
    bike_id integer NOT NULL,
    name_localizedvalue0 text COLLATE pg_catalog."default",
    user_type text COLLATE pg_catalog."default",
    birth_year integer,
    gender integer,
    CONSTRAINT trips_pkey PRIMARY KEY (start_time, bike_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE citibike.trips
    OWNER to postgres;