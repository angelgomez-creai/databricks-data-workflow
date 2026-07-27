from pyspark import pipelines as dp

silver_schema = spark.conf.get("silver_schema")


@dp.table(
    name=f"{silver_schema}.date_dim",
    comment="Cleaned date dimension, deduplicated on d_date_sk.",
    cluster_by=["d_year"],
)
@dp.expect_or_drop("valid_date_sk", "d_date_sk IS NOT NULL")
def silver_date_dim():
    return (
        spark.readStream.table("date_dim")
        .dropDuplicates(["d_date_sk"])
        .drop("_source_table")
    )
