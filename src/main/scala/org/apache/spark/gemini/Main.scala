package org.apache.spark.gemini

/**
  * Created by xinni on 7/9/16.
  */
import org.apache.spark.util.Utils
import org.apache.spark.{SparkConf, SparkContext}
import py4j.GatewayServer


object Main extends App {

  var sc: SparkContext = null

  def getSc(): SparkContext = sc

  override def main(args: Array[String]): Unit = {
    println(args)
    val conf = new SparkConf()
    sc = new SparkContext(conf)
    val gatewayServer = new GatewayServer(Main, 10050)
    val thread = new Thread(new Runnable {
      override def run(): Unit = Utils.logUncaughtExceptions {
        gatewayServer.start()
      }
    })
    thread.setName("py4j-gateway-init")
    thread.setDaemon(true)
    thread.start()
    thread.join()
    println(gatewayServer.getListeningPort)
    val rddData = sc.parallelize(List.range(1, 200))
    println(rddData.collect())
  }

}
