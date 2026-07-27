from pyspark import pipelines as dp
from pyspark.sql import functions as F

SOURCE_TABLE = "samples.tpcds_sf1.store_sales"


@dp.table(
    name="store_sales",
    comment="Raw store_sales fact, ingested as-is from samples.tpcds_sf1.store_sales.",
    cluster_by=["ss_sold_date_sk"],
)
def bronze_store_sales():
    return (
        spark.readStream.table(SOURCE_TABLE)
        .withColumn("_ingested_at", F.current_timestamp())
        .withColumn("_source_table", F.lit(SOURCE_TABLE))
    )
