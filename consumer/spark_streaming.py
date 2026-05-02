from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, IntegerType, StringType

spark = SparkSession.builder \
    .appName("KafkaStreaming") \
    .getOrCreate()

schema = StructType() \
    .add("order_id", IntegerType()) \
    .add("amount", IntegerType()) \
    .add("status", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders_topic") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

filtered_df = json_df.filter(col("status") == "SUCCESS")

query = filtered_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
