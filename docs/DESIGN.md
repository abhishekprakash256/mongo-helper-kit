# Mongo Helper Kit - Design Document

## 1. Overview
The **Mongo Helper Kit** is a Python package designed to simplify interactions with MongoDB. It provides a range of helper functions to handle database connections, perform CRUD operations, and manage chat-based message storage. This package is intended to streamline development by abstracting repetitive code and ensuring cleaner, more maintainable database interactions.

## 2. Dependencies
- **MongoDB client**: The MongoDB client instance (`mongo_client`) is initialized in `connection.py` and imported for use in other modules.
- **Python Standard Libraries**:
  - `datetime`: Used to timestamp messages in chat-related operations.
  - `traceback`: For error handling and debugging.
  - `os` and `subprocess`: May be used for managing the environment, configuration, or subprocesses if necessary.

## 3. Package Architecture
The Mongo Helper Kit is organized into modular components, each focusing on specific functionalities. This modularity allows users to import only the necessary modules and maintain a clear separation of concerns.

### Project Structure
```
mongo-helper-kit/
├── mongo_helper_kit/
│   ├── __init__.py
│   ├── connection.py           # Handles MongoDB connections
│   ├── mongo_crud_operations.py # Provides CRUD operations
│   ├── utils.py                # Helper functions (e.g., logging, utility functions)
│   └── config.py               # Configuration management
├── tests/                      # Unit tests for each module
├── examples/                   # Example usage scripts
└── requirements.txt            # Package dependencies
```

### Key Modules
- **connection.py**: Manages MongoDB connections.
- **mongo_crud_operations.py**: Contains functions for core CRUD (Create, Read, Update, Delete) operations and message-related operations.
- **utils.py**: Provides utility functions such as logging and other commonly used helper functions.
- **config.py**: Manages configuration settings (e.g., database URIs, environment variables).

Each module is designed to be reusable, maintainable, and modular, allowing users to integrate only the required functionalities.

## 4. Core Components and Functionalities

### 4.1 Database Connection (connection.py)
This module manages the connection to MongoDB, establishing a MongoDB client instance that other modules can use for database interactions.

#### Example Functions:
- `connect_to_db(uri)`: Establishes a MongoDB connection with the provided URI.
- `close_connection(client)`: Closes the MongoDB client connection.

### 4.2 CRUD Operations (mongo_crud_operations.py)
This module provides basic CRUD functionalities. It is implemented as a class `Helper_fun` that encapsulates all MongoDB operations to ensure easy access and reuse.

#### Class: `Helper_fun`
This class provides methods to handle common MongoDB operations, including creating databases, collections, and performing CRUD operations.

- **`__init__(self, client=mongo_client)`**  
  Initializes the `Helper_fun` instance with a MongoDB client.
  
#### CRUD Methods
1. **`make_database_and_collection(self, db_name, db_collection)`**  
   - **Description**: Creates a new database and collection if they do not already exist.
   - **Parameters**:
     - `db_name` (str): The name of the database.
     - `db_collection` (str): The name of the collection within the database.

2. **`make_collections(self, db_name, collection_name)`**  
   - **Description**: Creates a collection in an existing database if it doesn’t exist.
   
3. **`show_collections(self, db_name)`**  
   - **Description**: Lists all collections in a specific database.
   
4. **`show_all_data(self, db_name, collection_name)`**  
   - **Description**: Displays all documents in a specified collection.

5. **`insert_data(self, db_name, collection_name, data)`**  
   - **Description**: Inserts a new document into a specified collection, provided it doesn't already exist.
   
6. **`delete_data(self, db_name, collection_name, data)`**  
   - **Description**: Deletes a document matching `data` from a collection.

7. **`modify_data_one(self, db_name, collection_name, filter_criteria, new_data)`**  
   - **Description**: Updates a document matching `filter_criteria` with `new_data`.
   
8. **`delete_db(self, db_name)`**  
   - **Description**: Deletes the specified database.
   
9. **`delete_data_all(self, db_name, collection_name)`**  
   - **Description**: Deletes all documents in a specified collection.

### 4.3 Chat Application Support
The package includes support for chat-based applications, allowing for message storage, retrieval, and deletion.

#### Chat Functions
1. **`insert_message_data(self, db_name, collection_name, chat_hash, sender_hash, recipient_hash, message)`**
   - **Description**: Inserts a message document with sender and recipient information.
   - **Parameters**:
     - `chat_hash` (str): Unique identifier for the chat.
     - `sender_hash` (str): Identifier for the message sender.
     - `recipient_hash` (str): Identifier for the recipient.
     - `message` (str): Message content.

2. **`get_chat_messages(self, db_name, collection_name, chat_hash)`**
   - **Description**: Retrieves all messages in a chat sorted by timestamp.

3. **`delete_message(self, db_name, collection_name, chat_hash)`**
   - **Description**: Deletes all messages associated with the specified `chat_hash`.

### 4.4 Utility Functions (utils.py)
Provides common helper functions, such as logging and error handling.

- **`log_error(error_message)`**: Logs errors with timestamps.
- **`print_traceback()`**: Outputs the traceback for debugging.

### 4.5 Configuration (config.py)
Handles configuration management for database URIs and other environment variables. This module centralizes settings for easy modification.

#### Example Configuration:
- `DB_URI`: URI for MongoDB connection.
- `DEFAULT_DB_NAME`: Default database name, if needed.

## 5. Error Handling
Error handling is primarily done using the `traceback` module to print error messages. This approach ensures traceability of issues. For production-level code, it’s advisable to implement structured logging.

## 6. Testing and Examples
- **tests/**: Contains unit tests for all modules to ensure functionality.
- **examples/**: Contains example scripts demonstrating the usage of core functions, such as connecting to MongoDB, creating databases, and using CRUD operations.

## 7. Usage Example

```python
from mongo_helper_kit.mongo_crud_operations import Helper_fun


# Establish connection
db_helper = Helper_fun()

# Create a database and collection
db_helper.make_database_and_collection("test_db", "test_collection")

# Insert data
db_helper.insert_data("test_db", "test_collection", {"name": "Example", "value": 123})

# Show all data
db_helper.show_all_data("test_db", "test_collection")
```

## 8. Future Enhancements
- **Advanced Querying**: Add support for more complex MongoDB queries.
- **Bulk Operations**: Implement batch insert and update for improved performance on large datasets.
- **Enhanced Error Handling**: Use structured logging and exception handling.
- **User Authentication**: Add support for MongoDB authentication and user management.
- **Documentation and Typing**: Improve inline documentation and type annotations for better usability.

## 9. Conclusion
The Mongo Helper Kit aims to simplify MongoDB interactions by providing a set of reusable, modular, and maintainable components for database and chat-related operations. With clear error handling, configuration management, and essential CRUD functionalities, this package helps developers focus on business logic while minimizing boilerplate code.

## 10. Note

The client name passed in the helper fucntion is imp as using from outside use - "localhost"
The client name passed in the helper fucntion is imp as using from docker container use - "mongo"

--- 

This document includes details on the architecture, modules, error handling, and examples, offering a complete overview of the Mongo Helper Kit for easy understanding and future maintenance.