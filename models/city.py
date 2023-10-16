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
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        This method initializes the parameters
        """
        super().__init__(*args, **kwargs)
