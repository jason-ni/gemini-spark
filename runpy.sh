SPARK_HOME=$(dirname `which spark-submit`)
export SPARK_HOME=$(dirname $SPARK_HOME)

export PYSPARK_HOME=$SPARK_HOME/python

export PYTHONPATH=$PYSPARK_HOME/lib/pyspark.zip:$PYSPARK_HOME/lib/py4j-0.9-src.zip

python $@


