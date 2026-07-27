from pyspark import pipelines as dp

silver_schema = spark.conf.get("silver_schema")
gold_schema = spark.conf.get("gold_schema")


@dp.materialized_view(
    name=f"{gold_schema}.dim_item",
    comment="Item dimension for BI consumption.",
)
def gold_dim_item():
    return spark.read.table(f"{silver_schema}.item").select(
        "i_item_sk",
        "i_item_id",
        "i_item_desc",
        "i_current_price",
        "i_wholesale_cost",
        "i_brand",
        "i_class",
        "i_category",
        "i_manufact",
        "i_product_name",
    )
