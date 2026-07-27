from pyspark import pipelines as dp

silver_schema = spark.conf.get("silver_schema")
gold_schema = spark.conf.get("gold_schema")


@dp.materialized_view(
    name=f"{gold_schema}.dim_store",
    comment="Store dimension for BI consumption.",
)
def gold_dim_store():
    return spark.read.table(f"{silver_schema}.store").select(
        "s_store_sk",
        "s_store_id",
        "s_store_name",
        "s_city",
        "s_county",
        "s_state",
        "s_zip",
        "s_country",
        "s_division_name",
        "s_company_name",
        "s_market_desc",
        "s_number_employees",
        "s_floor_space",
    )
