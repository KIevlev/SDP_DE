CREATE DATABASE IF NOT EXISTS SDP;
USE SDP;
CREATE TABLE food(
order_id int,
quantity int,
item_name String,
choice_description String,
item_price String
)
row format delimited fields terminated by ','
TBLPROPERTIES('serialization.null.format'='','skip.header.line.count'='1');

LOAD DATA INPATH '/user/hue/data.csv' OVERWRITE INTO TABLE food;

SELECT item_name, count(*) as quantity FROM food GROUP BY item_name ORDER BY quantity DESC LIMIT 5;

