from pyspark import SparkContext, SparkConf
import re

config = SparkConf().setAppName("griboedov").setMaster("yarn")
sc = SparkContext(conf=config)
a = sc.accumulator(0)
rdd = sc.textFile("/data/griboedov")
rdd = rdd.map(lambda x: re.sub(u"\\W+", " ", x.strip(), flags=re.U))
rdd = rdd.filter(lambda x: len(x)>3 and x.istitle())
rdd2 = rdd.map(lambda x: x.strip())
rdd2_1 = rdd2.filter(lambda x: re.sub(u"\\W+", " ", x, flags=re.U))
rdd3 = rdd2_1.flatMap(lambda x: x.split(" "))
rdd4 = rdd3.map(lambda x: (x,1))
rdd5 = rdd4.reduceByKey(lambda a, b: a + b)\
    .sortBy(lambda a: -a[1])
def f(x):
    global a
    a += 1

words_count = rdd5.foreach(f)
print(str(words_count))

