from azure.storage.blob import BlobClient
import os
class BlobStorageClient:
        
    def __init__(self) -> None:
        
        self.blob_client_object = BlobClient.from_connection_string(os.environ.get("BLOB_STORAGE_CONNECTION_STRING"),
                                                                    container="word-cloud-images", blob="word-cloud-image")

        