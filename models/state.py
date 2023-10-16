#!/usr/bin/python3
"""
Module: state

This module containa a classState that inherits from BaseModel.
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    This class inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        This method initializes the parameter
        """
        super().__init__(*args, **kwargs)
