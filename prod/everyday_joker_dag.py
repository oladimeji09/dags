from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import sys, python_helper as ph
sys.path.insert(0,ph.root_fp+'everyday_joker')
import everyday_joker as jk

default_args = {
    'owner': 'airflow',
    'start_date':datetime(2022, 2, 6),
                }

with DAG('everyday_joker',
        schedule_interval ='30 19 * * *',
        default_args= default_args,
        tags =['everyday_joker','instgram'],
        catchup = True
        ) as dag:

        share_joke = PythonOperator(
            task_id = 'share_joke',
            python_callable = jk.share_joke,
            op_kwargs={"tags": 25}
            )

        # follow_and_comment = PythonOperator(
        #     task_id = 'follow_and_comment',
        #     python_callable = jk.follow_and_comment,
        #     op_kwargs={"tags": 1, "top_media": 1, "follow" : 'N'}
        #     )

        # unfollow_user = PythonOperator(
        #     task_id = 'unfollow_user',
        #     python_callable = jk.unfollow_user,
        #     op_kwargs={"users": 20}
        #     )

        share_joke 
