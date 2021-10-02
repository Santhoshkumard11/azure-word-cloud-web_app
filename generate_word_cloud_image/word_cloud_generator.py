from save_user_data.cosmos_db_client import CosmosDBClient

import logging

class WorldCloudGenerate:
    
    def __init__(self, cosmos_db_client_obj) -> None:
        
    
        self.cosmos_db_client_obj = cosmos_db_client_obj

    def get_all_names_from_cosmos_db(self):
        
        self.name_list = self.cosmos_db_client_obj.get_all_items()

    def


    def save_image_to_blob_storage(self):
        pass    
        
                
            
        
        
        