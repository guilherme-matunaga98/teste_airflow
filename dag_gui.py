from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator

default_args={
        "owner": "airflow",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    }

with DAG(
    dag_id="example_gui",
    default_args=default_args,
    start_date=datetime(2023, 10, 1),
    schedule_interval="@daily"
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo "Hello, World!"'
    )

    task1
