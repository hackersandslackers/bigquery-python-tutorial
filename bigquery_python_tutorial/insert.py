"""Create a table from CSV hosted on GCS."""
from google.cloud.bigquery import SourceFormat, LoadJobConfig
from google.api_core.exceptions import BadRequest
from google.cloud.bigquery.table import Table
from .clients import LOGGER, gbq
from config import GCP_BUCKET_NAME


def gcs_csv_to_table(
    project_id: str, dataset_id: str, table_id: str, remote_csv_path: str
) -> Table:
    """
    Insert CSV from Google Storage to BigQuery Table.

    :param project_id: Google Cloud project ID.
    :type project_id: str
    :param dataset_id: ID of Google BigQuery dataset.
    :type dataset_id: str
    :param table_id: ID of Google BigQuery table.
    :type table_id: str
    :param remote_csv_path: Path to uploaded CSV.
    :type remote_csv_path: str
    :returns: str
    """
    try:
        full_table_id = f"{project_id}.{dataset_id}.{table_id}"
        gcs_csv_uri = f"gs://{GCP_BUCKET_NAME}/{remote_csv_path}"
        job_config = LoadJobConfig(
            autodetect=True,
            skip_leading_rows=1,
            source_format=SourceFormat.CSV,
        )
        load_job = gbq.load_table_from_uri(
            gcs_csv_uri, full_table_id, job_config=job_config
        )
        LOGGER.info(f"Starting job {load_job.job_id}.")
        LOGGER.info(load_job.result())  # Waits for table load to complete.
        return gbq.get_table(full_table_id)
    except BadRequest as e:
        LOGGER.error(f"Invalid GCP request when creating table `{table_id}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error when creating table `{table_id}`: {e}")
