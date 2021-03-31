from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.check_operator import CheckOperator, IntervalCheckOperator, ValueCheckOperator

from trainig import training
#from evaluation import evaluate



with DAG(
    dag_id='test_airflow',
    description='ML project',
    schedule_interval='0 8 * * *',
    start_date=datetime(2020, 1, 6)
) as dag:
    install_modules_1 = BashOperator(
        task_id='install_modules_1',
        bash_command='pip install -U scikit-learn"',
        dag=dag
    )
    
    
    train_model = PythonOperator(
        task_id='train_model',
        python_callable=training,
        dag = dag
    )


