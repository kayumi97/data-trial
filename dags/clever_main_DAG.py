from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "alec.ventura",
    "start_date": datetime(2024, 10, 1),
}

datasets = [
    'fmcsa_complaints.csv',
    'fmcsa_safer_data.csv',
    'fmcsa_company_snapshot.csv',
    'fmcsa_companies.csv',
    'customer_reviews_google.csv',
    'company_profiles_google_maps.csv'

]

with DAG("clever_main_DAG", default_args=default_args, catchup=False, schedule_interval='20 0 * * *', max_active_runs=1) as dag:

    start_task = EmptyOperator(task_id='Start', dag=dag)
    finish_task = EmptyOperator(task_id='Finish', dag=dag)

    for file in datasets:
        file_without_extension = file.split('.')[0]

        task_id = f"upload_to_postgres_{file_without_extension}"
        upload_to_postgres_task = PythonOperator(
            task_id=task_id,
            python_callable=upload_to_postgres,
            dag=dag,
            execution_timeout=timedelta(milliseconds=2),
            op_kwargs={
                "file_name": file
            }
        )

        start_task.set_downstream(upload_to_postgres_task)
        upload_to_postgres_task.set_downstream(finish_task)
