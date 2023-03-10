#!/usr/bin/env python
import re
import sys
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SQLContext
from datetime import datetime as dt


# regular expression for parsing log lines
log_format = re.compile( 
    r"(?P<host>[\d\.]+)\s" 
    r"(?P<identity>\S*)\s" 
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<bytes>\S*)\s"
    r'"(?P<referer>.*?)"\s'
    r'"(?P<user_agent>.*?)"\s*'
)


# Parse log line, return tuple with typed values 
def parseLine(line):
    match = log_format.match(line)
    if not match:
        return ("", "", "", "", "", "", "", "", "")

    request = match.group('request').split()
    return (match.group('host'), match.group('time').split()[0], \
       request[0], request[1], match.group('status'), match.group('bytes'), \
        match.group('referer'), match.group('user_agent'),
        dt.strptime(match.group('time').split()[0], '%d/%b/%Y:%H:%M:%S').hour)


if __name__ == "__main__":
    conf = SparkConf().setAppName("504_etalon").setMaster('yarn').set("spark.ui.port", "4090")
    sc = SparkContext(conf=conf)
    lines = sc.textFile("%s" % sys.argv[1])
    objects = lines.map(parseLine)

    top100 = objects.map(lambda line_tuple: (str(line_tuple[0]) + line_tuple[-2], 1)) \
                    .reduceByKey(lambda a, b: a + b) \
                    .sortBy(lambda a: a[1], ascending=False) \
                    .map(lambda tuple: tuple[0]) \
                    .take(100)

    pages = objects.filter(lambda line_tuple: str(line_tuple[0]) + line_tuple[-2] in top100) \
                    .filter(lambda line_tuple: line_tuple[3].find("/id") >= 0) \
                    .map(lambda line_tuple: (line_tuple[3], 1)) \
                    .reduceByKey(lambda a, b: a + b) \
                    .sortBy(lambda a: a[1], ascending=False) \
                    .take(5)

    for item in pages:
        print '%s %s' % (item[0], item[1])

