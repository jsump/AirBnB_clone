#!/usr/bin/python3
"""
This module contains a class that serializes instances to JSON file
and deserializes JSON file to instances.
"""


import json
import importlib
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This method returns the objects created after deserialization
        """
        return self.__objects

    def new(self, obj):
        """
        This method creates a new object ot be serialized
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        This method saves the object that has been created
        """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """
        This method opens the file for deserialization
        """
        try:
            with open(self.__file_path, "r") as file:
                if os.stat(self.__file_path).st_size == 0:
                    return

                data = json.load(file)

                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review

                class_mapping = {
                        "BaseModel": BaseModel,
                        "User": User,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Place": Place,
                        "Review": Review
                }

                for key, obj_data in data.items():
                    class_name, obj_id = key.split(".")
                    obj_class = class_mapping[class_name]
                    obj = obj_class(**obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
