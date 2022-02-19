from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import sys
from python_helpers import python_helper as ph
from python_helpers import google_helper as gh
sys.path.insert(0,ph.root_fp+'everyday_joker')

default_args = {
    'owner': 'airflow',
    'start_date':datetime(2022, 2, 7),
                }
def timecheck():
    with open(ph.root_fp+'working_files/heartbeat/heartbeat.csv', 'a+') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M") +'\n')

def gmail_check():
    with open(ph.root_fp+'working_files/heartbeat/gmail_heartbeat.csv', 'a+') as f:
        print('LEVEL 1')
        try:
            if gh.main('gmail'):
                print('LEVEL 2')
                f.write('Gmail Active \t'+ datetime.now().strftime("%Y-%m-%d %H:%M")+'\n')
        except:
                f.write('Gmail Inactive \t'+ datetime.now().strftime("%Y-%m-%d %H:%M") +'\n')
                print('LEVEL 3')

with DAG('timecheck',
        schedule_interval = '@hourly',
        default_args= default_args,
        tags =['time_logger'],
        catchup = True
        ) as dag:

        heartbeat = PythonOperator(
            task_id = 'heartbeat',
            python_callable = timecheck
            )
        gmail_heartbeat = PythonOperator(
            task_id = 'gmail_heartbeat',
            python_callable = gmail_check
            )
        heartbeat >> gmail_heartbeat
