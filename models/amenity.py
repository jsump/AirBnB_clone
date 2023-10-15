#!/usr/bin/python3
"""
This module contains a class Amenity that inherits from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        This method initializes the parameter
        """
        super().__init__()
        self.name = ""

    def __str__(self):
        return f"Amenity: {self.name}"
