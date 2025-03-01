# LAB-1: Requirement Install Issue

## Follow the steps below to resolve a Python package dependency conflict in the lab environment

### Steps

Navigate to the project directory and edit the requirements.txt file:

```shell script
cd aws-mwaa-local-runner/
vim requirements/requirements.txt
```
Add the following content to requirements.txt:

```config
--constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.11.txt"

boto3==1.35.36
pyspark==3.5.3
apache-airflow-providers-mysql==6.0.0
```

Verify the Python dependencies by running:


```shell script
./mwaa-local-env test-requirements
```
You will encounter the following error:

```log
Container amazon/mwaa-local:2_10_3 exists. Skipping build
--constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.11.txt"
Installing requirements.txt
Requirement already satisfied: boto3==1.35.36 in ./.local/lib/python3.11/site-packages (from -r /usr/local/airflow/requirements/requirements.txt (line 3)) (1.35.36)
Collecting pyspark==3.5.3
  Downloading pyspark-3.5.3.tar.gz (317.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 317.3/317.3 MB 4.9 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
ERROR: Cannot install apache-airflow-providers-mysql==6.0.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested apache-airflow-providers-mysql==6.0.0
    The user requested (constraint) apache-airflow-providers-mysql==5.7.3

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
```


### Questions

How would you resolve the Python package dependency conflict shown in the error message above?


