import time
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator

import requests
import urllib.request
import ssl,os
import gzip
import dotenv
from config import rds_host,rds_password,rds_user,ip_list
from Modules.MySQL_module import SQL
today_date = datetime.today().date()
default_args = {
    'owner': 'Poyu',
    'start_date': datetime(2021, 6, 2, 0, 0),
    'schedule_interval': '@daily',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}


movie_database = SQL(user=rds_user,password=rds_password,host=rds_host,database="movie")
