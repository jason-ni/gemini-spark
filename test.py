from pyspark.java_gateway import launch_gateway
import pyspark

gw = launch_gateway()

sc = gw.entry_point.sc()

conf = pyspark.SparkConf(_jvm=gw.jvm, _jconf=sc.conf())

for x in conf.getAll():
    print x

jsc = gw.jvm.JavaSparkContext(sc)

pysc = pyspark.SparkContext(gateway=gw, jsc=jsc)

rdd = pysc.parallelize(range(1, 100))

print rdd.collect()

sqlContext = pyspark.sql.SQLContext(pysc)

df = sqlContext.read.json("people.json")

df.show()
