"""
The file to have supporting methods to perform CRUD operations in Mongo
"""

#imports
import subprocess
from datetime import datetime
import traceback
import os
from .connection import create_mongo_client




#make the mongo client 
#mongo_client = create_mongo_client("local")


#the helper class for the mongo functions 
# Helper class for MongoDB functions

class Helper_fun():

    def __init__(self, host_name=None, client=None):

        #create the mongo client
        if client is not None:
            self.mongo_client = client  # Use the provided mock client
        else:
            self.mongo_client = create_mongo_client(host_name)  # Create a real client with the host_name


    def make_database_and_collection(self, db_name, db_collection):
        """
        Make the database and collection if they don't exist
        """
        # Print the list of existing databases before attempting to create the database
        print("Existing databases before creating '{}':".format(db_name), self.mongo_client.list_database_names())

        # Make the database if it doesn't exist
        if db_name not in self.mongo_client.list_database_names():
            # Create the database
            db = self.mongo_client[db_name]

            # Create the collection
            collection = db[db_collection]

            # Insert dummy data into the collection
            dummy_data = {"dummy_data": True}
            insert_data = collection.insert_one(dummy_data)

            print("Database '{}' and collection '{}' created.".format(db_name, db_collection))
        else:
            # If the database exists, select it
            db = self.mongo_client[db_name]
            collection = db[db_collection]
            print("Database '{}' already exist.".format(db_name, db_collection))
        
        # Print the list of existing databases after attempting to create the database
        print("Existing databases after creating '{}':".format(db_name), self.mongo_client.list_database_names())



    def make_collections(self,db_name,collection_name):
        """
        The function to make the collection in the database
        """
        db = self.mongo_client[db_name]


        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print("Collection '{}' created.".format(collection_name))

        else:
            print("Collection '{}' already exists.".format(collection_name))



    def show_collections(self,db_name):
        """
        show the collections
        """
        db = self.mongo_client[db_name]

        collections = db.list_collection_names()

        for collection_lst in collections:
            print(collection_lst)
    

    def show_all_data(self,db_name,collection_name):
        """
        Show the data in the collection
        """
        db = self.mongo_client[db_name]
        collection = db[collection_name]


        if collection is not None:
            # Retrieve all documents in the collection
            documents = collection.find()

            # Print each document
            for document in documents:
                print(document)
        else:
            print("No collection available. Please create a collection first.")


    def make_index(self,db_name,collection_name):
        """
        The function to make the indexin in the database for articles data 
        """
        
        db = self.mongo_client[db_name]

        collection = db[collection_name]

        if collection is not None:

            db.collection.create_index([
                ("article_name", "text"),
                ("section_name", "text"),
                ("article_para", "text"),
                ("article_data.title", "text"),
                ("article_data.article_para", "text"),
                ("article_data.markdown_data", "text")
            ])

            return "Indexing is succesfull"
        
        return "Indexing data error"
        


    def show_article_data(self,db_name,collection_name,article_name):
        """
        Find the specific data from the collection
        depreciated now 
        """

        db = self.mongo_client[db_name]
        collection = db[collection_name]

        if collection is not None:
            # Retrieve all documents in the collection
            page_data = collection.find_one(article_name)
        
        return page_data


    def get_article_data(self,db_name,collection_name,section_name,article_name):
        """
        The function to fetch the article data from section in single collection
        use slug now   
        """
        db = self.mongo_client[db_name]
        collection = db[collection_name]

        if collection is not None:

            #search the query 
            query = {"section_name": section_name, "article_name":article_name }

            page_data = collection.find_one(query)

            if not page_data:

                return None
        
        return page_data


    def search_database(self,db_name,collection_name,keyword):
        """
        The function to search the database as per keyword and return as card data
        """   

        db = self.mongo_client[db_name]
        collection = db[collection_name]

        # Define the search filter using `$or` and `$regex`
        search_filter = {
            "$or": [
                {"article_name": {"$regex": keyword, "$options": "i"}},
                {"section_name": {"$regex": keyword, "$options": "i"}},
                {"article_para": {"$regex": keyword, "$options": "i"}},
                {"article_data.title": {"$regex": keyword, "$options": "i"}},
                {"article_data.article_para": {"$regex": keyword, "$options": "i"}},
                {"article_data.markdown_data": {"$regex": keyword, "$options": "i"}}
            ]
        }

        # Execute the query and return results (sorted by `created_at` field)
        searched_data = list(collection.find(search_filter).sort("created_at", -1))

        results = []

        for article in searched_data:
            # Extract the necessary fields based on the new design
            card = {
                "card_title": article.get("article_name", ""),
                "card_para": article.get("article_para", ""),
                "img_src": article.get("article_image", ""),
                "card_url": article.get("article_link", "")
            }
            results.append(card)

        return results

    

    def get_card_data(self,db_name,collection_name,section_name, limit):
        """
        The funcion to get the card data as per section name
        """

        db = self.mongo_client[db_name]
        collection = db[collection_name]

        # Query the MongoDB collection for articles in the specified section
        filtered_data = collection.find({"section_name": section_name}).limit(limit)
        
        result = []
        for article in filtered_data:
            # Extract the necessary fields based on the new design
            card = {
                "card_title": article.get("article_name", ""),
                "card_para": article.get("article_para", ""),
                "img_src": article.get("article_image", ""),
                "card_url": article.get("article_link", "")
            }
            result.append(card)
        
        return result




    def insert_data(self,db_name,collection_name,data):
        """
        Insert the data into the database and collection
        """
        db = self.mongo_client[db_name]
        collection = db[collection_name]

        #if the data is None 
        if data is None:
            return "data is Null"
        

        # Check if any documents match the criteria
        existing_data = collection.find_one(data)

        if existing_data is None:
        
        #insert the data
            
            for page_data in data:
                insert_data_res = collection.insert_one(page_data)

        #condtion to check for the data is inserted 
            if insert_data_res.acknowledged :
                print("Data inserted succesfuly")
    
            else:
                print("Data not inserted")
        
        else:
            print("Data  already exist")


    def delete_data(self,db_name,collection_name,data):
        """
        The function to delete the data
        """
        #if the data is None 
        if data is None:
            return "data is Null"
        
        db = self.mongo_client[db_name]
        collection = db[collection_name]

        # Check if any documents match the criteria
        existing_data = collection.find_one(data)

        # Delete a single document that matches the criteria
        delete_result = collection.delete_one(data)

        if delete_result.deleted_count == 1:
            print("Data deleted successfully.")
        else:
            print("No record matched the data")

    def modify_data_one(self,db_name,collection_name,filter_criteria,new_data):
        """
        The function to modify the data in mongodb as per collection and db
        """

        #if the data is None 
        if new_data is None:
            return "data is Null"
    
        db = self.mongo_client[db_name]
        collection = db[collection_name]
    
        #update the data in collection
        if collection.update_one(filter_criteria,new_data):  # Update the data 
            print("Update succesfull")
        
        else:
            print("Update failed")

    def delete_db(self,db_name):
        """
        The function to delete the database
        """
        db = self.mongo_client[db_name]
        
        #drop the database
        self.mongo_client.drop_database(db_name)

        print("The database has been deleted")
    

    def delete_data_all(self,db_name,collection_name):
        """
        The funciton to delete all the data inside a collection
        """
        pass



    # the chat app data fetching methods  --- 

    def insert_message_data(self,db_name,collection_name,chat_hash,sender_hash, recipient_hash, message):
        """
        The funciton to insert the message in the database and collection
        """
        db = self.mongo_client[db_name]
        collection = db[collection_name]

        message_doc = {
        'chat_hash': chat_hash,
        'sender_hash': sender_hash,
        'recipient_hash': recipient_hash,
        'message': message,
        'timestamp': datetime.now()
        }

        if collection.insert_one(message_doc):
            print("Succesfull insertion")
        else:
            print("failed to insert message")
    
    def get_chat_messages(self,db_name,collection_name,chat_hash):
        """
        The function to get the messages from the database
        """

        db = self.mongo_client[db_name]
        collection = db[collection_name]


        return collection.find({'chat_hash': chat_hash}).sort('timestamp', 1)

    def delete_message(self, db_name, collection_name, chat_hash):
        """
        The function to delete messages based on chat_hash
        """
        db = self.mongo_client[db_name]
        collection = db[collection_name]

        try:
            # delete the data
            delete_result = collection.delete_many({'chat_hash': chat_hash})

            if delete_result.deleted_count > 0:
                print("Chat data erased")
            else:
                print("No records found to delete")
        except Exception as e:
            print(f"Error deleting message: {e}")
            traceback.print_exc()