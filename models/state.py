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
    def __init__(self):
        """
        This method initializes the parameter
        """
        super().__init__()
        self.name = ""

    def __str__(self):
        """
        This method ensures that the input name is a string
        """
        return f"State: {self.name}"
