#!/usr/bin/python3
"""
Module: user

This module contains a class User that inherits from BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    This class inherits from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        This method initializes the parameter
        """
        super().__init__(*args, **kwargs)
