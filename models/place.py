#!/usr/bin/python3
"""
Module: place

This module contains a aclass Place that inherits from BaseModel
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    This class inherits from BaseModel
    """
    def __init__(self):
        """
        this method initializes the parameters
        """
        super().__init__()
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    def __str__(self):
        """
        this ensures the input are strings
        """
        return (
                f"Place: Name - {self.name}, "
                f"Description - {self.description}, "
                f"Number of rooms - {self.number_rooms}, "
                f"Number of bathrooms - {self.number_bathrooms}, "
                f"Max Guests - {self.max_guest}, "
                f"Price per night - {self.price_by_night}, "
                f"Latitude - {self.latitude}, "
                f"Longitude - {self.longitude}, "
                f"Amenity IDs - {self.amenity_ids}"
        )
