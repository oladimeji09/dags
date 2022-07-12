from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import sys
from python_helpers import python_helper as ph
from python_helpers import google_helper as gh
sys.path.insert(0,ph.root_fp+'docx_pdf')
import worker as wk

default_args = {
    'owner': 'airflow',
    'start_date':datetime(2022, 2, 20),
                }

with DAG('docx_pdf',
        schedule_interval ='*/30 * * * *',
        default_args= default_args,
        tags =['testing','converting','email','sherlock'],
        catchup = False
        ) as dag:

        create_pdfs = PythonOperator(
            task_id = 'send_email',
            python_callable = wk.create_test,
            )

        create_pdfs
