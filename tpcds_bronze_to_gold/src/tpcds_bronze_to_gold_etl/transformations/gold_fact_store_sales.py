from pyspark import pipelines as dp

silver_schema = spark.conf.get("silver_schema")
gold_schema = spark.conf.get("gold_schema")


@dp.materialized_view(
    name=f"{gold_schema}.fact_store_sales",
    comment=(
        "Conformed store_sales fact. Grain: one row per (ss_ticket_number, ss_item_sk). "
        "FKs reference dim_store (ss_store_sk), dim_customer (ss_customer_sk), "
        "dim_item (ss_item_sk), and dim_date (ss_sold_date_sk)."
    ),
)
def gold_fact_store_sales():
    return spark.read.table(f"{silver_schema}.store_sales").select(
        "ss_ticket_number",
        "ss_item_sk",
        "ss_sold_date_sk",
        "ss_store_sk",
        "ss_customer_sk",
        "ss_quantity",
        "ss_wholesale_cost",
        "ss_list_price",
        "ss_sales_price",
        "ss_ext_discount_amt",
        "ss_ext_sales_price",
        "ss_ext_wholesale_cost",
        "ss_ext_list_price",
        "ss_ext_tax",
        "ss_coupon_amt",
        "ss_net_paid",
        "ss_net_paid_inc_tax",
        "ss_net_profit",
    )
