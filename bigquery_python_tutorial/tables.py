"""Fetch tables from Google Cloud project."""
from typing import List, Optional, Sequence, Union, Mapping, Any
import pprint
from google.cloud.bigquery.table import Table
from google.cloud.bigquery.schema import SchemaField
from google.api_core.exceptions import BadRequest
from .clients import LOGGER, gbq


def list_all_tables() -> List[Optional[Table]]:
    """
    List all BigQuery tables in a Google Cloud project.

    :returns: List[Optional[Table]]
    """
    tables = []
    for dataset in gbq.list_datasets():
        for listed_table in gbq.list_tables(dataset.dataset_id):
            table = get_table(
                listed_table.project, listed_table.dataset_id, listed_table.table_id
            )
            tables.append(table)
    return tables


def get_table(project_id: str, dataset_id: str, table_id: str) -> Table:
    """
    Get a single Google BigQuery table.

    :param project_id: Google Cloud project ID.
    :type project_id: str
    :param dataset_id: ID of Google BigQuery dataset.
    :type dataset_id: str
    :param table_id: ID of Google BigQuery table.
    :type table_id: str
    :returns: Table
    """
    try:
        full_table_id = f"{project_id}.{dataset_id}.{table_id}"
        table = gbq.get_table(full_table_id)
        LOGGER.info(f"{dataset_id}.{table_id}: {table.num_rows} rows.")
        return table
    except BadRequest as e:
        LOGGER.error(f"Invalid GCP request when fetching table `{table_id}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error when fetching table `{table_id}`: {e}")


def get_table_schema(table: Table) -> Sequence[Union[SchemaField, Mapping[str, Any]]]:
    """
    Get BigQuery Table Schema.

    :param table: Google BigQuery table object.
    :type table: Table
    :returns: Sequence[Union[SchemaField, Mapping[str, Any]]]
    """
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(table.schema)
    return table.schema
