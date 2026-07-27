# tpcds_bronze_to_gold

Bronze -> silver -> gold pipeline for the `samples.tpcds_sf1` star schema, implementing
[angelgomez-creai/databricks-data-workflow#1](https://github.com/angelgomez-creai/databricks-data-workflow/issues/1).

Source tables (all read from the read-only `samples.tpcds_sf1` schema): `store_sales` (fact),
`store`, `customer`, `item`, `date_dim` (dimensions).

This folder defines all source code for the `tpcds_bronze_to_gold` pipeline:

- `explorations/`: Ad-hoc notebooks used to explore the data processed by this pipeline.
- `transformations/`: All dataset definitions and transformations, one file per table, named
  `<layer>_<table>.py` (e.g. `bronze_store_sales.py`, `silver_store.py`, `gold_dim_item.py`).

## Layers

| Layer | Tables | Notes |
|---|---|---|
| Bronze | `store_sales`, `store`, `customer`, `item`, `date_dim` | Raw 1:1 ingestion from `samples.tpcds_sf1`, plus `_ingested_at`/`_source_table` columns. Written to `${bronze_schema}` (pipeline default schema). |
| Silver | `store_sales`, `store`, `customer`, `item`, `date_dim` | Deduplicated on primary key, non-null key expectations. Written to `${silver_schema}`. |
| Gold | `dim_store`, `dim_customer`, `dim_item`, `dim_date`, `fact_store_sales`, `agg_daily_sales_by_store` | Conformed star schema plus a daily sales-by-store summary. Written to `${gold_schema}`. |

All output tables are created in the `workspace` catalog (see `../../databricks.yml` for the
`catalog`/`bronze_schema`/`silver_schema`/`gold_schema` variables).

## Getting Started

* If you're using the workspace UI, use `Run file` to run and preview a single transformation.
* If you're using the CLI, use `databricks bundle run tpcds_bronze_to_gold_etl --refresh store_sales`
  to run a single transformation (unqualified name = bronze table name).
* `databricks bundle validate` checks the bundle before deploying.
* `databricks bundle deploy` deploys the pipeline; `databricks bundle run tpcds_bronze_to_gold_etl` runs it.

For syntax reference, see https://docs.databricks.com/dlt/python-ref.html.
