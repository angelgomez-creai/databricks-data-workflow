from pyspark import pipelines as dp
from pyspark.sql import functions as F

SOURCE_TABLE = "samples.tpcds_sf1.item"


@dp.table(
    name="item",
    comment="Raw item dimension, ingested as-is from samples.tpcds_sf1.item.",
)
def bronze_item():
    return (
        spark.readStream.table(SOURCE_TABLE)
        .withColumn("_ingested_at", F.current_timestamp())
        .withColumn("_source_table", F.lit(SOURCE_TABLE))
    )
