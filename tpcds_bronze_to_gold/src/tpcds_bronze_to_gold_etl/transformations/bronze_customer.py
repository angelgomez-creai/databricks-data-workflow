from pyspark import pipelines as dp
from pyspark.sql import functions as F

SOURCE_TABLE = "samples.tpcds_sf1.customer"


@dp.table(
    name="customer",
    comment="Raw customer dimension, ingested as-is from samples.tpcds_sf1.customer.",
)
def bronze_customer():
    return (
        spark.readStream.table(SOURCE_TABLE)
        .withColumn("_ingested_at", F.current_timestamp())
        .withColumn("_source_table", F.lit(SOURCE_TABLE))
    )
