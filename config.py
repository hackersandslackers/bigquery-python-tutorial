"""BigQuery Upload Configuration."""
from os import environ


# Google Cloud Storage
bucket_uri = environ.get('GCP_BUCKET_URI')
bucket_name = environ.get('GCP_BUCKET_NAME')

# Google BigQuery
bigquery_dataset = environ.get('GCP_BIGQUERY_DATASET')
bigquery_table = environ.get('GCP_BIGQUERY_TABLE')

# Data
local_data_csv = environ.get('LOCAL_DATA_TARGET')
destination_blob = environ.get('DESTINATION_BLOB_NAME')
