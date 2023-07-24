# sales_etl_dag.py

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from extraction import extract_data
from transformation import transform_data
from loading import load_data

default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'sales_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for sales data',
    schedule_interval=timedelta(days=1),  # Daily schedule
)

# Task 1: Data Extraction
def extract():
    csv_file_path = '/path/to/your/csv/file.csv'
    return extract_data(csv_file_path)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract,
    dag=dag,
)

# Task 2: Data Transformation
def transform(**kwargs):
    ti = kwargs['ti']
    extracted_data = ti.xcom_pull(task_ids='extract_data')
    transformed_data = transform_data(extracted_data)
    return transformed_data

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform,
    provide_context=True,
    dag=dag,
)

# Task 3: Data Loading
def load(**kwargs):
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids='transform_data')
    db_connection_string = 'mysql://user3:salesdbpwd@localhost/salesdb'
    table_name = 'sales_data'
    load_data(transformed_data, db_connection_string, table_name)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load,
    provide_context=True,
    dag=dag,
)

# Define task dependencies
extract_task >> transform_task >> load_task
