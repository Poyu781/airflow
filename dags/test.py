import sys
import os,json
import time
import re
import urllib
from pprint import pprint
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from collections import defaultdict
from difflib import SequenceMatcher
sys.path.extend(["/Users/poyuchiu/Desktop/airflow-movieon"])
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from modules import crawl
from modules import mail_notification
from modules.mysql_module import SQL
from modules.imdb_fetch import IMDb_fetch,BASE_DIR,movie_mongo_db
from config import rds_host,rds_password,rds_user
movie_new_db =  SQL(user=rds_user,password=rds_password,host=rds_host,database="movie_new")
default_args = {
    'owner': 'Poyu',
    'start_date': datetime(2021, 6, 26, 0, 0),
    'schedule_interval': '@hourly',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}
today_date = datetime.today().date()



def test():
    x =  movie_new_db.fetch_list("select * from imdb_rating limit 1 ")
    print(x)
    return x


with DAG('123', default_args=default_args,catchup=False) as dag:
    
    test = PythonOperator(
        task_id = "test",
        python_callable = test
    )

    test
