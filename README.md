
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
```

Or install directly via pip (if available on PyPI):


## Usage

```
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

## Examples



## Configuration

- Clients 
    - "mongo" is passed when using insiede the docker conatienr to acces the mongo
    - "localhost" is passed when using outside the docker container to access the mongo for bulk data insertion



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this blueprint as needed, depending on your library’s specific features and usage!