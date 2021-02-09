"""Create a BigQuery table, view a table schema, list all tables in a project."""
from .clients import LOGGER, gcs, gbq
from .tables import list_all_tables, get_table_schema, get_table
from .insert import gcs_csv_to_table
from .storage import upload_csv_data
from config import (
    LOCAL_CSV_FILEPATH,
    REMOTE_CSV_DESTINATION,
    GCP_PROJECT_ID,
    GCP_BIGQUERY_DATASET_ID,
    GCP_BIGQUERY_TABLE_ID,
    GCP_BUCKET_NAME,
)


def init_script():
    """Initiate script."""

    blob = upload_csv_data(LOCAL_CSV_FILEPATH, GCP_BUCKET_NAME, REMOTE_CSV_DESTINATION)

    # Insert CSV as new BigQuery table
    table = gcs_csv_to_table(
        GCP_PROJECT_ID, GCP_BIGQUERY_DATASET_ID, GCP_BIGQUERY_TABLE_ID, blob.name
    )

    # Print schema of newly created table
    get_table_schema(table)

    # List all tables in project
    list_all_tables()
