from pyspark import pipelines as dp

silver_schema = spark.conf.get("silver_schema")


@dp.table(
    name=f"{silver_schema}.store",
    comment="Cleaned store dimension, deduplicated on s_store_sk.",
)
@dp.expect_or_drop("valid_store_sk", "s_store_sk IS NOT NULL")
def silver_store():
    return (
        spark.readStream.table("store")
        .dropDuplicates(["s_store_sk"])
        .drop("_source_table")
    )
