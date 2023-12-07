import pandas as pd
import psycopg2 as psql
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def connect_database(**kwargs):
    connection = psql.connect(
        # user='airflow',
        # password='airflow',
        # host='postgres',
        # port='5432',
        # dbname='airflow'

        user='airflow',
        password='airflow',
        host='localhost',
        port='5432',
        dbname='airflow'
    )

    df = pd.read_sql("select * from gold_history ", connection)
    df.to_csv('/opt/airflow/dags/gold_history_raw.csv')

    df = pd.read_sql("select * from GOLD_stock_data ", connection)
    df.to_csv('/opt/airflow/dags/GOLD_stock_data_raw.csv')

    df = pd.read_sql("select * from kgc_stock_data ", connection)
    df.to_csv('/opt/airflow/dags/kgc_stock_data_raw.csv')

    df = pd.read_sql("select * from nem_stock_data ", connection)
    df.to_csv('/opt/airflow/dags/nem_stock_data_raw.csv')

    df = pd.read_sql("select * from rgld_stock_data ", connection)
    df.to_csv('/opt/airflow/dags/rgld_stock_data_raw.csv')

    df = pd.read_sql("select * from sand_stock_data ", connection)
    df.to_csv('/opt/airflow/dags/sand_stock_data_raw.csv')
    print("-------Data Saved------")


connect_database()