from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import sys
from python_helpers import python_helper as ph
sys.path.insert(0,ph.root_fp+'automated_ig_pages/forbes_tracker')
import forbes_tracker as jk

default_args = {
    'owner': 'airflow',
    'start_date':datetime(2022, 2, 2),
                }

with DAG('forbes_tracker',
        schedule_interval ='15 16 * * 1-5',
        default_args= default_args,
        tags =['forbes_tracker','instgram','ig'],
        catchup = False
        ) as dag:

        share_img = PythonOperator(
            task_id = 'share_img',
            python_callable = jk.upload_media,
            op_kwargs={"num_rich_ppl": 10}
            )

        delete_media = PythonOperator(
            task_id = 'delete_media',
            python_callable = jk.ig.delete_media,
            op_kwargs={"username": jk.creds.get('user_name'),
                    "password": jk.creds.get('password'), "N":10 }
            )
        # unfollow_user = PythonOperator(
        #     task_id = 'unfollow_user',
        #     python_callable = jk.unfollow_user,
        #     op_kwargs={"users": 20}
        #     )

        # follow_and_comment = PythonOperator(
        #     task_id = 'follow_and_comment',
        #     python_callable = jk.follow_and_comment,
        #     op_kwargs={"tags": 3, "top_media": 5, "follow" : 'N'}
        #     )
        delete_media >> share_img   # >> follow_and_comment >> unfollow_user


# /bin/bash -c 'airflow initdb; \
#             airflow scheduler'
#
# /bin/bash -c 'airflow webserver'
