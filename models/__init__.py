#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine import db_storage
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity

from os import environ

dummy_classes = {"BaseModel": BaseModel, "User": User,
                 "Review": Review, "City": City,
                 "State": State, "Place": Place,
                 "Amenity": Amenity}

dummy_tables = {"states": State, "cities": City,
                "users": User, "places": Place,
                "reviews": Review, "amenities": Amenity}

storage_engine = environ.get("HBNB_TYPE_STORAGE")

if (storage_engine == "db"):
    storage = db_storage.DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
