import os
from google.cloud import bigquery

def create_bqclient(access_key_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = access_key_path
    client = bigquery.Client().from_service_account_json(access_key_path)
    return client