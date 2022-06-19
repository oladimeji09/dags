from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import sys
from python_helpers import python_helper as ph
from python_helpers import google_helper as gh
sys.path.insert(0,ph.root_fp+'automated_ig_pages/le_bad_joker')
import le_bad_joker as jk

default_args = {
    'owner': 'airflow',
    'start_date':datetime(2022, 2, 27),
                }

with DAG('le_bad_joker',
        schedule_interval ='@daily',
        default_args= default_args,
        tags =['le_bad_joker','instgram'],
        catchup = False
        ) as dag:

        share_joke = PythonOperator(
            task_id = 'share_joke',
            python_callable = jk.share_joke,
            op_kwargs={"tags": 25}
            )

        follow_and_comment = PythonOperator(
            task_id = 'follow_and_comment',
            python_callable = jk.follow_and_comment,
            op_kwargs={"subject":"comedy", "tags": 1, "top_media": 1, "follow" : 'N'}
            )
#
#         # unfollow_user = PythonOperator(
#         #     task_id = 'unfollow_user',
#         #     python_callable = jk.unfollow_user,
#         #     op_kwargs={"users": 20}
#         #     )
#
        share_joke >>  follow_and_comment
