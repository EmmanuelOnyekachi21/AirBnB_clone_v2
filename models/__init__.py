#!/usr/bin/python3
"""This module instantiates a storage object."""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Define the Storage variable
storage = None

def initialize_storage():
    """
    Initialize the storage system based on the environment variable.
    """
    global storage
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        storage = DBStorage()
    else:
        storage = FileStorage()
    storage.reload()

initialize_storage()
