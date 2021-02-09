"""Instantiate Google Cloud Storage Client."""
from google.cloud import storage
from config import GCP_PROJECT_ID


gcs = storage.Client(GCP_PROJECT_ID)
