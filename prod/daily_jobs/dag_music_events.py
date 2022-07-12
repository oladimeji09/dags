# from airflow import DAG
# from datetime import datetime
# from airflow.operators.python import PythonOperator
# import sys, pandas as pd
# from python_helpers import python_helper as ph
# from python_helpers import google_helper as gh
#
# default_args = {
#     'owner': 'airflow',
#     'start_date':datetime(2022, 5, 7),
#                 }
#
# def main():
#     """Delete google calendar events then insert new events from DF"""
#     dl = ph.creds.get('emails')
#     sh = gh.open_wb('1Vc7RkGbbk9THM6AeU2vBMpBOnSlDzpyrFNI9Mp4rWz0').worksheet('Data')
#     gh.delete_events(dl.get('email2'),'***')
#     for row in sh.get_all_records():
#         if row['Event Date']:
#             try:
#                 body = {
#                     "summary":'*** '+ row['Event'],
#                     "description": str(row),
#                     "start":    {"date": str(pd.to_datetime(row['Event Date']).date()), "timeZone": 'Europe/London'},
#                     "end":      {"date": str(pd.to_datetime(row['Event Date']).date()  + pd.Timedelta(days=1)), "timeZone": 'Europe/London'},
#                     "attendees":    [{ "email": dl.get('email1')
#                                     # "responseStatus": "needsAction"
#                                     }
#                                     ],
#                     "reminders": {
#                                 "useDefault": False,
#                                 "overrides": [
#                                             # {"method": "email", "minutes": 24 * 60},
#                                             {"method": "popup", "minutes": 24 * 60},
#                                             {"method": "popup", "minutes": 24*7 * 60},
#                                             ],
#                                 },
#                 }
#                 gh.insert_events(dl.get('email2'),body,'all')
#                 print('inserting event for ' +row['Event'])
#             except:
#                 continue
#
# with DAG('music_events',
#         schedule_interval = '@daily',
#         default_args= default_args,
#         tags =['events','calendar','music'],
#         catchup = False
#         ) as dag:
#
#         events = PythonOperator(
#             task_id = 'events',
#             python_callable = main
#             )
#
#         events
