from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import sys
from python_helpers import python_helper as ph
from python_helpers import google_helper as gh
sys.path.insert(0,ph.root_fp+'docx_pdf')
import testing as pt

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

        share_img = PythonOperator(
            task_id = 'send_email',
            python_callable = pt.create_test,
            )

        share_img
