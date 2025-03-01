# Broken DAGs

## Follow the steps below to resolve a broken DAG issue in the lab environment

Edit the lab DAG file on your local laptop:

```
vim els_lab2_dag.py
```

Copy and paste the following code into the els_lab2_dag.py file:

```python
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
    
```

Upload the DAG file to S3 bucket:

```shell script
aws s3 cp els_lab2_dag.py s3://<BUCKET_NAME>/els_mwaa_2025/
```

Connect to your Linux instance via SSH:

```shell script
ssh -i key-pair.pem ec2-user@ec2-x-x-x-x.compute-1.amazonaws.com
```

Download the DAG file from S3 bucket:

```shell script
aws s3 cp s3://<BUCKET_NAME>/els_mwaa_2025/els_lab2_dag.py ./
```

Copy the DAG file to the DAGs folder:

```shell script
cp els_lab2_dag.py aws-mwaa-local-runner/dags/
```

Check Airflow UI (wait approximately 5 minutes for DAG file processing), you may encounter the following error:

![](lab2_DAG_Import_Errors.png)

```log
Broken DAG: [/usr/local/airflow/dags/lth_lab2_dag.py]
Traceback (most recent call last):
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/usr/local/airflow/dags/lth_lab2_dag.py", line 5, in <module>
    from airflow.providers.apache.spark.operators.spark_jdbc import SparkJDBCOperator
ModuleNotFoundError: No module named 'airflow.providers.apache'
```


### Questions

1. How to resolve the "ModuleNotFoundError" issue?
2. How to check the DAG processing logs in the container?
