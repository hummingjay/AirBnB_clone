#!/usr/bin/python3
" this script is the bsaemodel of the console """

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ This is the constructor method for BaseModel class.
        The '__init__' method is called when a new instance
        of class is created and initializes:
            - 'id':a string representation of a unique identifier
             using 'uuid.uuid4()' function
            - 'created_at': a datetime object representing creation time
            - 'updated_at': a datetime object reprenting the current d&t
            this is updated whenever save() method is called.
        Args:
            - *args: variable number of arguments
            - **args: dict of key-value arguments

        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Returns a string representation of the object"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Public instance method that updates instance attr updated_at """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Public instance method returning dict with all keys of __dict__
        name of the dict: my_dict
        copy: creates a copy of the objects attr dict
        __class__ : special key to store name of object's class - this will
        help when deserializing the dict rep of the object
        __name__: returns the name of class as string
        converts created and update at to ISO format using isoformat() method
        of datetime objects and returns the modified dict
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
