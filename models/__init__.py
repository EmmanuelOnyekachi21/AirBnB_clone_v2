#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine import db_storage
from models.engine.file_storage import FileStorage
import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = db_storage.DBStorage()
else:
    storage = FileStorage()

storage.reload()
