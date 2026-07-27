from pyspark import pipelines as dp

silver_schema = spark.conf.get("silver_schema")


@dp.table(
    name=f"{silver_schema}.store_sales",
    comment="Cleaned store_sales fact. Grain: one row per (ss_ticket_number, ss_item_sk).",
    cluster_by=["ss_sold_date_sk"],
)
@dp.expect_or_drop("valid_item_sk", "ss_item_sk IS NOT NULL")
@dp.expect_or_drop("valid_ticket_number", "ss_ticket_number IS NOT NULL")
@dp.expect_or_drop("non_negative_quantity", "ss_quantity IS NULL OR ss_quantity >= 0")
def silver_store_sales():
    return (
        spark.readStream.table("store_sales")
        .dropDuplicates(["ss_ticket_number", "ss_item_sk"])
        .drop("_source_table")
    )
