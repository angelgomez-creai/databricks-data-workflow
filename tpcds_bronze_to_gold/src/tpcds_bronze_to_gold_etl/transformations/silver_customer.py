from pyspark import pipelines as dp

silver_schema = spark.conf.get("silver_schema")


@dp.table(
    name=f"{silver_schema}.customer",
    comment="Cleaned customer dimension, deduplicated on c_customer_sk.",
)
@dp.expect_or_drop("valid_customer_sk", "c_customer_sk IS NOT NULL")
def silver_customer():
    return (
        spark.readStream.table("customer")
        .dropDuplicates(["c_customer_sk"])
        .drop("_source_table")
    )
