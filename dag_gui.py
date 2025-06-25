from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator

with DAG(
    dag_id="example_gui",
    start_date=datetime(2023, 10, 1),
    schedule_interval="@daily",
    default_args={
        "owner": "airflow",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    catchup=False,  # Evita execução retroativa desde 2023
    tags=["example"]
) as dag:

    start = DummyOperator(task_id="start")
    end = DummyOperator(task_id="end")

    start >> end
