"""Programmatically create a BigQuery table from a CSV."""
import pprint
from google.cloud import storage
from google.cloud import bigquery
from loguru import logger
from config import (
    bucket_uri,
    bucket_name,
    bigquery_dataset,
    bigquery_table,
    local_data_csv,
    destination_blob
)


def main():
    """Initiate script."""
    storage_upload_blob(
        bucket_name,
        local_data_csv,
        destination_blob
    )
    bigquery_insert_data(
        bucket_uri,
        destination_blob,
        bigquery_dataset,
        bigquery_table
    )
    bigquery_table_schema = get_table_schema(
        bigquery_dataset,
        bigquery_table
    )
    # Print Schema to Console
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(bg_table.schema)


def storage_upload_blob(bucket_name, source_file_name, destination_blob):
    """Upload a CSV to Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(source_file_name)
    return f'File {source_file_name} uploaded to {destination_blob}.'


def bigquery_insert_data(bucket_uri, destination_blob, dataset_id, table_id):
    """Insert CSV from Google Storage to BigQuery Table."""
    target = bucket_uri + destination_blob
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.skip_leading_rows = 1
    job_config.source_format = bigquery.SourceFormat.CSV
    load_job = bigquery_client.load_table_from_uri(
        target,
        dataset_ref.table(table_id),
        job_config=job_config
    )
    logger.info('Starting job {}'.format(load_job.job_id))
    load_job.result()  # Waits for table load to complete.
    return 'Job finished.'


def get_table_schema(dataset_id, table_id):
    """Get BigQuery Table Schema."""
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    bg_tableref = bigquery.table.TableReference(dataset_ref, table_id)
    bg_table = bigquery_client.get_table(bg_tableref)
    return bg_table.schema


main()