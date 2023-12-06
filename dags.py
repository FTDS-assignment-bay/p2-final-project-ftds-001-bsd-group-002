import pandas as pd
import psycopg2 as psql
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator