#!/usr/bin/python3
"""
Module: base_model

This module contains a class that defines common attributes/methods
for other classes.
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This class defines all common attributes/methods for other
    classes.
    """
    def __init__(self, *args, **kwargs):
        """
        This method initializes parameters
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            self.id = kwargs.get('id', str(uuid.uuid4()))

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                )
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                )
        else:
            storage.new(self)

    def __str__(self):
        """
        This method prints the class name, id and dictionary
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates the public instance attribute "updated_at"
        with the current datetimee.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This method returns a dictionary containing all key/values of
        __dict__ of the instance: by using self.__dict__, a key __class_,
        created_at, updated_at.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
