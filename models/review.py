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
    def __init__(self):
        """
        This method initializes parameters
        """
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def __str__(self):
        """
        This method returns the string represetnaion of the instance
        """
        return (
                f"Review: Place ID - {self.place_id}, "
                f"User ID - {self.user_id}, "
                f"Text - {self.text}"
        )
