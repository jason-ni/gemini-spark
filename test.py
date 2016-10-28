from pyspark.java_gateway import launch_gateway
import pyspark
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

gw = launch_gateway()

sc = gw.entry_point.sc()
sqlc = gw.entry_point.sqlc()
jsession = gw.entry_point.ss()

conf = pyspark.SparkConf(_jvm=gw.jvm, _jconf=sc.conf())

for x in conf.getAll():
    print x

jsc = gw.jvm.JavaSparkContext(sc)

pysc = pyspark.SparkContext(gateway=gw, jsc=jsc)

rdd = pysc.parallelize(range(1, 100))

print rdd.collect()

sqlContext = pyspark.sql.SQLContext(pysc,
                                    sparkSession=SparkSession(
                                        pysc, jsparkSession=jsession),
                                    jsqlContext=sqlc)

df = sqlContext.read.json("people.json")

df.show()

schema = StructType([StructField("name", StringType(), True),
                     StructField("age", IntegerType(), True)])

nameAgeRDD = pysc.parallelize([("Amy", 8), ("Tom", 10)])
df = nameAgeRDD.toDF(schema=schema)
df.show()
