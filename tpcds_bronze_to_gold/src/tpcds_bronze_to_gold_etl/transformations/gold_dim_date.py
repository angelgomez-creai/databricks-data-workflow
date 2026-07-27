from pyspark import pipelines as dp

silver_schema = spark.conf.get("silver_schema")
gold_schema = spark.conf.get("gold_schema")


@dp.materialized_view(
    name=f"{gold_schema}.dim_date",
    comment="Date dimension for BI consumption.",
)
def gold_dim_date():
    return spark.read.table(f"{silver_schema}.date_dim").select(
        "d_date_sk",
        "d_date",
        "d_year",
        "d_moy",
        "d_dom",
        "d_dow",
        "d_day_name",
        "d_quarter_name",
        "d_week_seq",
        "d_weekend",
        "d_holiday",
    )
