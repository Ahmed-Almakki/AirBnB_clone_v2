#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class amenity inhirent form BaseMole"""
    def __init__(self, *args):
        self.name = args[0]
