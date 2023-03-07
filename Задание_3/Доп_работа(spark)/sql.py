from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
sqlContext = SQLContext(sc)
data = sqlContext.read.csv("/user/out-ievlev-ko/data.csv", inferSchema=True, header=True)
grouped = data.groupBy("item_name")
grouped.count().sort(desc("count")).show(5)