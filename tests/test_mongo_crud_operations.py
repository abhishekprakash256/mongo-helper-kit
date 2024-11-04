"""
The file to test the mongo crud opertations 
"""


# tests/test_helper_fun.py

import pytest
import mongomock
from mongo_helper_kit import Helper_fun


@pytest.fixture
def mock_mongo_client():
    # Create a mock MongoDB client using mongomock
    client = mongomock.MongoClient()
    yield client
    client.close()


@pytest.fixture
def helper(mock_mongo_client):
    # Create an instance of Helper_fun with the mock client
    return Helper_fun(client=mock_mongo_client)



def test_make_database_and_collection(helper):
    # Test creating a database and collection
    helper.make_database_and_collection('test_db', 'test_collection')
    
    assert 'test_db' in helper.mongo_client.list_database_names()
    assert 'test_collection' in helper.mongo_client['test_db'].list_collection_names()


def test_make_collections(helper):
    # Test creating a collection
    helper.make_database_and_collection('test_db', 'test_collection')
    helper.make_collections('test_db', 'test_collection')  # Should not create again

    assert 'test_collection' in helper.mongo_client['test_db'].list_collection_names()



def test_show_article_data(helper):
    # Test showing specific article data
    helper.make_database_and_collection('test_db', 'test_collection')
    helper.insert_data('test_db', 'test_collection', [{'name': 'Alice'}, {'name': 'Bob'}])
    
    result = helper.show_article_data('test_db', 'test_collection', {'name': 'Alice'})
    
    assert result['name'] == 'Alice'


def test_insert_data(helper):
    # Test inserting data into the collection
    helper.make_database_and_collection('test_db', 'test_collection')
    result = helper.insert_data('test_db', 'test_collection', [{'name': 'Alice'}])
    
    assert result is None  # Check that no errors occurred
    assert helper.mongo_client['test_db']['test_collection'].count_documents({'name': 'Alice'}) == 1


def test_delete_data(helper):
    # Test deleting data from the collection
    helper.make_database_and_collection('test_db', 'test_collection')
    helper.insert_data('test_db', 'test_collection', [{'name': 'Alice'}])
    
    helper.delete_data('test_db', 'test_collection', {'name': 'Alice'})
    
    assert helper.mongo_client['test_db']['test_collection'].count_documents({'name': 'Alice'}) == 0


def test_modify_data_one(helper):
    # Test modifying data in the collection
    helper.make_database_and_collection('test_db', 'test_collection')
    helper.insert_data('test_db', 'test_collection', [{'name': 'Alice', 'age': 25}])
    
    helper.modify_data_one('test_db', 'test_collection', {'name': 'Alice'}, {'$set': {'age': 26}})
    updated_document = helper.show_article_data('test_db', 'test_collection', {'name': 'Alice'})
    
    assert updated_document['age'] == 26


def test_delete_db(helper):
    # Test deleting a database
    helper.make_database_and_collection('test_db', 'test_collection')
    
    helper.delete_db('test_db')
    
    assert 'test_db' not in helper.mongo_client.list_database_names()


def test_delete_data_all(helper):
    # Test deleting all data in a collection (not implemented in original class)
    helper.make_database_and_collection('test_db', 'test_collection')
    helper.insert_data('test_db', 'test_collection', [{'name': 'Alice'}, {'name': 'Bob'}])
    
    # Implement the delete_data_all method in the Helper_fun class and test it here
    # Example:
    # helper.delete_data_all('test_db', 'test_collection')
    # assert helper.mongo_client['test_db']['test_collection'].count_documents({}) == 0


def test_insert_message_data(helper):
    # Test inserting a message
    helper.make_database_and_collection('chat_db', 'messages')
    helper.insert_message_data('chat_db', 'messages', 'chat1', 'user1', 'user2', 'Hello, world!')
    
    assert helper.mongo_client['chat_db']['messages'].count_documents({'message': 'Hello, world!'}) == 1


def test_get_chat_messages(helper):
    # Test getting chat messages
    helper.make_database_and_collection('chat_db', 'messages')
    helper.insert_message_data('chat_db', 'messages', 'chat1', 'user1', 'user2', 'Hello, world!')
    helper.insert_message_data('chat_db', 'messages', 'chat1', 'user2', 'user1', 'Hi there!')
    
    messages = list(helper.get_chat_messages('chat_db', 'messages', 'chat1'))
    
    assert len(messages) == 2  # Should retrieve 2 messages


def test_delete_message(helper):
    # Test deleting a chat message
    helper.make_database_and_collection('chat_db', 'messages')
    helper.insert_message_data('chat_db', 'messages', 'chat1', 'user1', 'user2', 'Hello, world!')
    
    helper.delete_message('chat_db', 'messages', 'chat1')
    
    assert helper.mongo_client['chat_db']['messages'].count_documents({'message': 'Hello, world!'}) == 0

