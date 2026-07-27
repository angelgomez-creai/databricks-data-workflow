from pyspark import pipelines as dp

silver_schema = spark.conf.get("silver_schema")


@dp.table(
    name=f"{silver_schema}.item",
    comment="Cleaned item dimension, deduplicated on i_item_sk.",
)
@dp.expect_or_drop("valid_item_sk", "i_item_sk IS NOT NULL")
def silver_item():
    return (
        spark.readStream.table("item")
        .dropDuplicates(["i_item_sk"])
        .drop("_source_table")
    )
