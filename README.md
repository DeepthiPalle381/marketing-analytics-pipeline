# Marketing Analytics Pipeline (Bank Telemarketing Data)

This project builds a dimensional-model-based analytics pipeline on top of a real bank marketing dataset. It transforms raw customer and campaign contact data into clean dimension and fact tables and computes key marketing KPIs such as conversion rates and campaign performance.

## Goals
- Ingest raw bank marketing data (train/test CSVs)
- Clean and standardize customer and campaign attributes
- Build a star schema:
  - dim_customer
  - dim_campaign
  - fact_marketing_interactions
- Compute marketing performance metrics (conversion rates, contact efficiency, etc.)
- Add data quality tests and an Airflow DAG for orchestration

