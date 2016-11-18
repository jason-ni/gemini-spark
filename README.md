This is a simple demo to show how to reuse the SparkContext of a Scala Spark driver in a remote Python script.

Run following commands to see the demo:

1. sbt assembly
2. Run "spark-submit target/scala-2.11/GeminiSpark-assembly-1.0.jar" in another console.
3. ./runpy.sh test.py
