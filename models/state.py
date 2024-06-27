#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    def __init__(self, *args):
        super().__init__()
        name, arg = args[0]
        self.name = name
        for ke, val in arg.items():
            setattr(self, ke, val)
