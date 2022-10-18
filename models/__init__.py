#!/usr/bin/python3
"""Instantiates a storage object
-> If the environment variable 'HBNB_TYPE_STORAGE' is set to 'db',
    instantiates to a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage)
"""
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
