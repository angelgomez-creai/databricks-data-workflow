from pyspark import pipelines as dp
from pyspark.sql import functions as F

SOURCE_TABLE = "samples.tpcds_sf1.date_dim"


@dp.table(
    name="date_dim",
    comment="Raw date dimension, ingested as-is from samples.tpcds_sf1.date_dim.",
    cluster_by=["d_year"],
)
def bronze_date_dim():
    return (
        spark.readStream.table(SOURCE_TABLE)
        .withColumn("_ingested_at", F.current_timestamp())
        .withColumn("_source_table", F.lit(SOURCE_TABLE))
    )
