from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.check_operator import CheckOperator, IntervalCheckOperator, ValueCheckOperator

from trainig import training
from evaluation import evaluate

CONN_IDCONN_ID = 'dev_postgres'


with DAG(
    dag_id='test_airflow',
    description='ML project',
    schedule_interval='0 8 * * *',
    start_date=datetime(2020, 1, 6)
) as dag:
    enter_point = DummyOperator(
        task_id='enter_point'
    )
