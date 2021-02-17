"""Fetch tables & table schemas."""
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
    LOGGER.info("LISTING ALL TABLES IN PROJECT:")
    for dataset in gbq.list_datasets():
        for listed_table in gbq.list_tables(dataset.dataset_id):
            table = get_table(
                f"{listed_table.project}.{listed_table.dataset_id}.{listed_table.table_id}"
            )
            tables.append(table)
    return tables


def get_table(full_table_id: str) -> Table:
    """
    Get a single Google BigQuery table.

    :param full_table_id: Full ID of a Google BigQuery table.
    :type full_table_id: str
    :returns: Table
    """
    try:
        table = gbq.get_table(full_table_id)
        LOGGER.info(f"{table.dataset_id}.{table.table_id}: {table.num_rows} rows.")
        return table
    except BadRequest as e:
        LOGGER.error(f"Invalid GCP request when fetching table `{full_table_id}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error when fetching table `{full_table_id}`: {e}")


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
