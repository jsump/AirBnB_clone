#!/usr/bin/python3
"""
Module: city

This module contains a class City that inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    This sclass inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        This method initializes the parameters
        """
        super().__init__()
        self.state_id = ""
        self.name = ""

    def __str__(self):
        """
        This method ensure that the input is a string
        """
        return f"City: {self.name}"
