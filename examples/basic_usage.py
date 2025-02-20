"""
The basic usage for the mongo client
"""
"""
The basic usage for the mongo client
"""
#CONST
DB_NAME = 'my_database'
COLLECTION_NAME = 'my_collection'
INSERTION_DATA = [{'name': 'Alice'}, {'name': 'Bob'}]

import mongo_helper_kit

# Create MongoDB client and initilaize the class for mongo methods
helper_fun = mongo_helper_kit.Helper_fun("localhost")  #use client name as localhost for bare metal and "mongo" for docker conaterin

# Create database and collection
helper_fun.make_database_and_collection(DB_NAME, COLLECTION_NAME)

# Insert data
helper_fun.insert_data(DB_NAME , COLLECTION_NAME , INSERTION_DATA)

# Show all data
print(helper_fun.show_all_data( DB_NAME, COLLECTION_NAME))

print(helper_fun.show_collections( DB_NAME))
