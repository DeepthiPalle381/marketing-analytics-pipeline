from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "deepthi",
    "start_date": datetime(2025, 1, 1),
    "retries": 1
}

with DAG(
    "marketing_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    bronze = BashOperator(
        task_id="ingest_raw_to_clean",
        bash_command="python src/ingest/ingest_marketing_data.py"
    )

    silver_gold = BashOperator(
        task_id="build_warehouse_tables",
        bash_command="python src/transform/transform_marketing_data.py"
    )

    bronze >> silver_gold
