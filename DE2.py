from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'Owner':'Jamshed',
    'start_date': days_ago(0),
    'email': ['jamshedparvez.tmc@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id = 'etl-log-processing-dagV1',
    default_args=default_args,
    description='This is my ETLfor server access log',
    schedule_interval=timedelta(days=1),
)

task1 = BashOperator(
    task_id= 'first_task',
    bash_command='data.ipynb',
    dag=dag
)

task1
