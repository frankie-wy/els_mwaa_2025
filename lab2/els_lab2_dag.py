import os
from datetime import datetime

from airflow.models import DAG
from airflow.providers.apache.spark.operators.spark_jdbc import SparkJDBCOperator
from airflow.providers.apache.spark.operators.spark_sql import SparkSqlOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

DAG_ID = os.path.basename(__file__).replace(".py", "")

with DAG(
    dag_id=DAG_ID,
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["mwaa","emr","spark"],
) as dag:
    
    
    # [START howto_operator_spark_submit]
    spark_submit_job = SparkSubmitOperator(
        task_id="spark_submit_job",
        deploy_mode="cluster",
        conn_id="spark_emr_conn",
        application="/usr/lib/spark/examples/src/main/python/pi.py",
        application_args=['1000'],
        name="SparkPi",
        verbose=False
    )
    # [END howto_operator_spark_submit]
    