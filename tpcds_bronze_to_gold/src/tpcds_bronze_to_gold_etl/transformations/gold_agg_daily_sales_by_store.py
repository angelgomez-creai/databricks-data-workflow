from pyspark import pipelines as dp
from pyspark.sql import functions as F

gold_schema = spark.conf.get("gold_schema")


@dp.materialized_view(
    name=f"{gold_schema}.agg_daily_sales_by_store",
    comment="Daily net sales, quantity, and order count by store, for reporting.",
)
def gold_agg_daily_sales_by_store():
    fact = spark.read.table(f"{gold_schema}.fact_store_sales")
    dim_date = spark.read.table(f"{gold_schema}.dim_date")
    dim_store = spark.read.table(f"{gold_schema}.dim_store")

    return (
        fact.join(dim_date, fact.ss_sold_date_sk == dim_date.d_date_sk, "inner")
        .join(dim_store, fact.ss_store_sk == dim_store.s_store_sk, "inner")
        .groupBy(dim_date.d_date, dim_store.s_store_id, dim_store.s_store_name)
        .agg(
            F.sum("ss_net_paid").alias("total_net_paid"),
            F.sum("ss_quantity").alias("total_quantity"),
            F.countDistinct("ss_ticket_number").alias("order_count"),
        )
    )
