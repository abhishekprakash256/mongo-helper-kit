
# Mongo Helper Kit

A collection of helper functions and utilities for MongoDB to simplify common database operations. This library provides reusable functions for database connections, CRUD operations, and other MongoDB interactions. That uses to mangane the operations in the Portfolio website 

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Easy-to-use helper functions for CRUD operations
- Simplified database connection handling
- Utility functions for bulk operations, indexing, and more
- Error handling and logging for MongoDB operations

## Installation

Clone the repository and install the required dependencies:

```bash
git clone git@github.com:abhishekprakash256/mongo-helper-kit.git
cd mongo-helper-kit
pip install -r requirements.txt

#installing through pip as a package , standard appraoch , after github auth done
pip install git+https://github.com/abhishekprakash256/mongo-helper-kit.git  

```

## Requirements 
```
mongomock==4.2.0.post1
pymongo==4.7.2
pytest==8.3.3
```

## Usage

### Notes 

**Docker or Bare Metal Mongo**

Can be used with docker or bare metal mongo install below are docker commands 

```bash

docker pull mongo

docker run -d --name mongo --network my_network -p 27017:27017 mongo:latest

```

```
from mongo_helper_kit.mongo_crud_operations import Helper_fun


# Establish connection
db_helper = Helper_fun("localhost")  #pass the name of the localhost

# Create a database and collection
db_helper.make_database_and_collection("test_db", "test_collection")

# Insert data
db_helper.insert_data("test_db", "test_collection", {"name": "Example", "value": 123})

# Show all data
db_helper.show_all_data("test_db", "test_collection")
```

### Run the module files

Use commands in python to run module file in examples dir from root dir 

python3 -m folder_name.file_name

```bash
python3 -m examples.basic_usage
```

### Run the test locally 

```bash
pytest

```
Run the command pytest in root directory

## Configuration

- Clients 
    - "mongo" is passed when using insiede the docker conatienr to acces the mongo
    - "localhost" is passed when using outside the docker container to access the mongo for bulk data insertion


## Note

The client name passed in the helper fucntion is imp as using from outside use - "localhost"
The client name passed in the helper fucntion is imp as using from docker container use - "mongo"

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
