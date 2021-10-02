import logging
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey



# Building a custom cosmos db client
class CosmosDBClient:
    def __init__(self, database_name: str, container_name: str):

        # get all the configurations to connect to the Cosmos DB
        self.HOST = cosmosdb_config.settings["host"]
        self.MASTER_KEY = cosmosdb_config.settings["master_key"]
        self.DATABASE_ID = ""
        self.CONTAINER_ID = ""

        self.database_name = database_name

        self.container_name = container_name

    def connect(self):
        """Initiate a connection to cosmos DB"""
        # connect with the cosmos DB client
        self.client = cosmos_client.CosmosClient(
            self.HOST,
            {"masterKey": self.MASTER_KEY},
            user_agent="CosmosDB",
            user_agent_overwrite=True,
        )

        # get the database connection object
        self.database = self.client.create_database_if_not_exists(id=self.database_name)

        # get the container connection object
        self.container = self.database.create_container_if_not_exists(
            id=self.container_name,
            partition_key=PartitionKey(path="/level"),
            offer_throughput=400,
        )

        logging.info("Successfully connected to CosmosDB")

    def add_item(self,item: dict):
        """Add new item to cosmos DB"""
        try:
            # create item in document from cosmos db
            self.container.create_item(body=item)

            logging.info(f"Successfully added the item to the database")

        except Exception as e:
            logging.error(f"Error while adding items to the container - {e}")
