"""BigQuery Configuration."""
from os import getenv, path
from dotenv import load_dotenv


# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# GCP Project
GCP_PROJECT_ID: str = getenv("GCP_PROJECT_ID")

# Google BigQuery
GCP_BIGQUERY_TABLE_ID: str = getenv("GCP_BIGQUERY_TABLE_ID")
GCP_BIGQUERY_DATASET_ID: str = getenv("GCP_BIGQUERY_DATASET_ID")

# Google Cloud Storage
GCP_BUCKET_URI: str = getenv("GCP_BUCKET_URI")
GCP_BUCKET_NAME: str = getenv("GCP_BUCKET_NAME")

# Data
LOCAL_CSV_FILEPATH: str = f"{basedir}/data/employees.csv"
REMOTE_CSV_DESTINATION: str = "datasets/employees.csv"
