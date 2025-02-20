"""
The test for mongo client
"""

#imports
import pytest
import mongo_helper_kit
import mongomock
from unittest.mock import patch


# imports
import pytest
import mongo_helper_kit
import mongomock
from unittest.mock import patch

@pytest.fixture
def mock_mongo_client():
    # Create a mock MongoDB client using mongomock
    client = mongomock.MongoClient()
    yield client
    client.close()

def test_mongodb_connection(mock_mongo_client):
    # Patch the function to return the mock client
    with patch("mongo_helper_kit.create_mongo_client", return_value=mock_mongo_client):
        client = mongo_helper_kit.create_mongo_client("mongo")

        # Test if the client can run a ping command successfully
        assert client.admin.command("ping")["ok"] != 0.0  # Check that the connection is okay.
