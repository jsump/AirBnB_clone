#!/usr/bin/python3
"""
Module: review

This module contains a class REview which inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        This method initializes parameters
        """
        super().__init__(*args, **kwargs)
