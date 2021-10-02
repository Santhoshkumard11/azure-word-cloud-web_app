import datetime
import logging

import azure.functions as func
from generate_word_cloud_image.blob_storage_client import BlobStorageClient

from generate_word_cloud_image.word_cloud_generator import WorldCloudGenerate

from save_user_data.cosmos_db_client import CosmosDBClient


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info("Generate word cloud trigger started!!")

    cosmos_db_client_obj = CosmosDBClient("WordCloudDB", "WordCloudUserTable")
    blob_client_obj = BlobStorageClient()

    cosmos_db_client_obj.connect()

    logging.info("Successfully connected with cosmos db!!")
    
    word_cloud_generate_obj = WorldCloudGenerate(cosmos_db_client_obj, blob_client_obj.get_blob_client)

    word_cloud_generate_obj.start_process()

    logging.info("Word Cloud generation process successfully completed!!")

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
