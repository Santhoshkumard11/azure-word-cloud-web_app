from wordcloud import WordCloud, STOPWORDS
import logging
import matplotlib.pyplot as plt


class WorldCloudGenerate:
    
    def __init__(self, cosmos_db_client_obj, blob_client_obj) -> None:
        
    
        self.cosmos_db_client_obj = cosmos_db_client_obj
        self.blob_client_obj = blob_client_obj
        
        self.names_only_list = []
        

    def query_all_item_from_cosmos_db(self):
        
        self.query_result = self.cosmos_db_client_obj.get_all_items()

    def get_all_names_from_cosmos_db(self):
        
        
        for item in self.query_result:
            
            
            self.names_only_list.append(item["name"])
        
        self.names_only_list = str(self.names_only_list)[1:-1].replace("'","").replace(",","")
        
        logging.info("Getting only the names from the item completed")

    def generate_word_cloud(self):
        
        self.word_cloud_obj = WordCloud(width = 800, height = 600,
                stopwords = STOPWORDS,
                min_font_size = 10).generate(self.names_only_list)

        self.image_object = self.word_cloud_obj.to_image()



    def save_image_to_blob_storage(self):
        
        self.blob_client_obj.upload_blob(self.image_object.tobytes(), blob_type="BlockBlob")    
    

    def start_process(self):
        self.query_all_item_from_cosmos_db()
        self.get_all_names_from_cosmos_db()
        self.generate_word_cloud()
        self.save_image_to_blob_storage()
        

        
        
        