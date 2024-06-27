#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    def __init__(self, *args):
        k = args[0]
        for ke, v in args[1].items():
            if ke == "state_id":
                state_id = v
        name = k
