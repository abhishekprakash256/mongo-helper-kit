"""
The test for mongo client
"""

#imports
import mongo_helper_kit



def test_mongodb_connection():
    #create the mongo clinet 
    client = mongo_helper_kit.create_mongo_client()

    #test the client
    assert client.admin.command("ping")["ok"] != 0.0  # Check that the connection is okay.



