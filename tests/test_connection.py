import pytest
#import mongomock
import mongo_helper_kit

from unittest.mock import patch, MagicMock
#from your_module import create_mongo_client  # Replace with actual module name

import mongo_helper_kit

client = mongo_helper_kit.create_mongo_client()
#helper = Helper_fun()

"""
# Test when the first host works
def test_create_mongo_client_first_host_success():
    with patch("mongo_helper_kit.create_mongo_client") as mock_client:
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.server_info.return_value = {}  # Simulate successful connection

        client = create_mongo_client()
        assert client is not None  # Should return a client
        assert mock_client.call_count == 1  # Only the first host should be tried

# Test when the second host works (first host fails)
def test_create_mongo_client_second_host_success():
    with patch("mongo_helper_kit.create_mongo_client") as mock_client:
        # First host connection fails
        mock_client.side_effect = [Exception("First host failure"), MagicMock()]

        client = create_mongo_client()
        assert client is not None  # Should return a client after second host
        assert mock_client.call_count == 2  # Both hosts are tried

# Test when both hosts fail
def test_create_mongo_client_failure():
    with patch("mongo_helper_kit.create_mongo_client", side_effect=Exception("Connection failed")) as mock_client:
        client = create_mongo_client()
        assert client is None  # Should return None after all hosts fail
        assert mock_client.call_count == 2  # Both hosts are tried
"""
