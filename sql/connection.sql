
-- Standard libpq connection string:
-- postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
-- 'postgresql://postgres:postgres@postgres.cx7bhejrlrq0.us-east-2.rds.amazonaws.com'

select dblink_connect('postgresql://postgres:postgres@postgres.cx7bhejrlrq0.us-east-2.rds.amazonaws.com:5342/postgres')