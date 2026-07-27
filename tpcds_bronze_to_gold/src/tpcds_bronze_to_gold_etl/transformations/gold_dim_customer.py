from pyspark import pipelines as dp

silver_schema = spark.conf.get("silver_schema")
gold_schema = spark.conf.get("gold_schema")


@dp.materialized_view(
    name=f"{gold_schema}.dim_customer",
    comment="Customer dimension for BI consumption.",
)
def gold_dim_customer():
    return spark.read.table(f"{silver_schema}.customer").select(
        "c_customer_sk",
        "c_customer_id",
        "c_salutation",
        "c_first_name",
        "c_last_name",
        "c_preferred_cust_flag",
        "c_birth_day",
        "c_birth_month",
        "c_birth_year",
        "c_birth_country",
        "c_email_address",
    )
