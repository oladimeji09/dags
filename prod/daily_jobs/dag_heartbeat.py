from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import sys, pandas as pd
from python_helpers import python_helper as ph
from python_helpers import google_helper as gh
default_args = {
    'owner': 'airflow',
    'start_date':datetime(2022, 2, 19),
                }

wb  = '1tZZqHg66wshrg5quUvOt_Etiqcea50putP3nDd5ueSk'

def timecheck():
    with open(ph.root_fp+'working_files/heartbeat/heartbeat.csv', 'a+') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M") +'\n')
    df= pd.read_csv(ph.root_fp+'working_files/heartbeat/heartbeat.csv')
    df = df[::-1]
    gh.rep_data_sh(df,wb,'main server')

def gmail_check():
    with open(ph.root_fp+'working_files/heartbeat/gmail_heartbeat.csv', 'a+') as f:
        try:
            if gh.main('gmail'):
                f.write('Gmail Active \t'+ datetime.now().strftime("%Y-%m-%d %H:%M")+'\n')
        except:
                f.write('Gmail Inactive \t'+ datetime.now().strftime("%Y-%m-%d %H:%M") +'\n')
    df= pd.read_csv(ph.root_fp+'working_files/heartbeat/gmail_heartbeat.csv', sep=('\t'))
    df = df[::-1]
    gh.rep_data_sh(df,wb,'gmail')

with DAG('heartbeat',
        schedule_interval = '@hourly',
        default_args= default_args,
        tags =['time_logger','heartbeat'],
        catchup = False
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
