from typing import Optional
from google.cloud.storage.blob import Blob
from .clients import LOGGER, gcs


def upload_csv_data(
    csv_filepath: str, bucket_name: str, blob_destination: str
) -> Optional[Blob]:
    """
    Upload a CSV to Google Cloud Storage.

    :param csv_filepath: Filepath to local CSV to create BigQuery from.
    :type csv_filepath: str
    :param bucket_name: Name of Google Cloud Storage.
    :type bucket_name: str
    :param blob_destination: Remote path to store new blob.
    :type blob_destination: str
    :returns: Blob
    """
    try:
        bucket = gcs.get_bucket(bucket_name)
        blob = bucket.blob(blob_destination)
        blob.upload_from_filename(csv_filepath)
        LOGGER.success(
            f"Successfully uploaded `{csv_filepath}` to `{blob_destination}`."
        )
        return blob
    except Exception as e:
        LOGGER.error(f"Unexpected error while uploading CSV: {e}")
