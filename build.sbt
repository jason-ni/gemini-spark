name := "GeminiSpark"
version := "1.0"
scalaVersion := Version.scala

libraryDependencies ++= Seq(
    "org.apache.spark" %% "spark-core"      % Version.spark % "provided",
    "org.apache.spark" %% "spark-sql"       % Version.spark % "provided",
    "org.apache.spark" %% "spark-hive"      % Version.spark % "provided",
    "org.apache.spark" %% "spark-catalyst"  % Version.spark % "provided",
    "org.apache.spark" %% "spark-streaming" % Version.spark % "provided",
    "net.sf.py4j"      % "py4j"            % "0.9"         % "provided"
)
