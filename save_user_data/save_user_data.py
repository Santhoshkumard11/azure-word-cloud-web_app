from .cosmos_db_client import CosmosDBClient

import logging

def save_user_data(user_name:str, associate_id: int, associate_level:str):
    
    try:
            
        # cosmos_db_client = CosmosDBClient("WordCloudDB", "WordCloudUserTable")

        # cosmos_db_client.connect()
        
        new_item_dict = {"name": user_name,
            "associate_id": associate_id,
            "level": associate_level} 
            

        # cosmos_db_client.add_item(new_item_dict)
        print(new_item_dict)
        return "success", "none"
    except:
        
        logging.exception("An exception occurred while saving user data")
        
    