"""
The mongo connection file to make the mongo clinet based on either running on the docker container or bare metal 
the client use as - localhost (outside of docker container ) or mongo (using other apps inside docekr container ) 

"""


#imports 
from pymongo import MongoClient


#new code
def create_mongo_client():
    hosts = ['localhost', 'mongo']  # List of hosts to try
    for host in hosts:
        try:
            # Try connecting to MongoDB using the current host
            client = MongoClient(host, 27017, serverSelectionTimeoutMS=2000)  # 2-second timeout
            client.server_info()  # This forces a connection attempt.
            print(f"MongoDB client created successfully using host: {host}")
            return client
        except Exception as e:
            print(f"Failed to connect to MongoDB using host {host}: {e}")
    
    # If neither host works, raise an exception or return None
    print("Failed to create MongoDB client with all host options.")
    return None




