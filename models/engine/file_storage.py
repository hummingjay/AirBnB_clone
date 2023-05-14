#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:
    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objectives[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()},
                      file)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist
        no exception should be raised)
        """
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf=8") as f:
            my_dict = json.load(f)
            my_dict = {k: self.classes()[v["__class__"]](**v) for k, v
                       in obj_dict.items()}
            # TODO:should this overwrite or insert?
            self.__objects = my_dict

    def attributes(self):
        """ Returns the valid attributes and their types for classname"""
        attributes = {
                "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
                "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
                "State":
                     {"name": str}.
                "City":
                     {"state_id": str,
                      "name": str},
                "Amenity":
                     {"name": str},
                "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "amenity_ids": list},
                "Review":
                {"place_id": str,
                    "user_id": str,
                    "text": str}
                }
        return attributes
