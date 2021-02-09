# Google BigQuery Python SDK Tutorial


![Python](https://img.shields.io/badge/Python-v3.8-blue.svg?logo=python&longCache=true&logoColor=white&style=flat-square&colorA=4c566a&colorB=5e81ac)
![Google Cloud BigQuery](https://img.shields.io/badge/Google--BigQuery-v1.27.2-blue.svg?logo=Google&longCache=true&logoColor=white&style=flat-square&colorA=4c566a&colorB=5e81ac)
![Google Cloud Storage](https://img.shields.io/badge/Google--Cloud--Storage-v1.31.0-blue.svg?logo=Google&longCache=true&logoColor=white&style=flat-square&colorA=4c566a&colorB=5e81ac)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/bigquery-python-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/bigquery-python-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/bigquery-python-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/bigquery-python-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/bigquery-python-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/bigquery-python-tutorial/network)

![Google BigQuery Python SDK](https://raw.githubusercontent.com/hackersandslackers/bigquery-python-tutorial/master/.github/bigquery_create_table%402x.jpg)

Source for the accompanying tutorial: https://hackersandslackers.com/google-bigquery-python/

# Getting Started

Get set up locally in two steps:

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `GCP_PROJECT_ID`: ID of your Google Cloud Project.
* `GOOGLE_APPLICATION_CREDENTIALS`: Filepath to JSON containing Google Cloud credentials as service key.
* `GCP_BUCKET_NAME`: Name of an existing Google Cloud Storage bucket (used to upload CSV dataset).
* `GCP_BIGQUERY_DATASET_ID`: Desired BigQuery dataset ID (can be new or existing).
* `GCP_BIGQUERY_TABLE_ID`: Desired BigQuery table name/ID (should be new table name).

*Remember never to commit secrets saved in .env files to Github.*

### Installation

Get up and running with `make deploy`:

```shell
$ git clone https://github.com/hackersandslackers/bigquery-python-tutorial.git
$ cd bigquery-python-tutorial
$ make deploy
``` 

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.