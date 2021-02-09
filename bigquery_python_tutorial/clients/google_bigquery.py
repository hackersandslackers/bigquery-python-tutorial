"""Instantiate Google BigQuery Client."""
from google.cloud import bigquery as google_bigquery
from config import GCP_PROJECT_ID


gbq = google_bigquery.Client(project=GCP_PROJECT_ID)
