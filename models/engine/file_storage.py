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
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    if class_name == "User":
                        module_name = "models.user"
                    elif class_name == "State":
                        module_name = "models.state"
                    elif class_name == "City":
                        module_name = "models.city"
                    elif class_name == "Place":
                        module_name = "models.place"
                    elif class_name == "Amenity":
                        module_name = "models.amenity"
                    elif class_name == "Review":
                        module_name = "models.review"
                    else:
                        module_name = "models.base_model"
                    module = __import__(module_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
