#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from os import getenv

class Amenity(BaseModel, Base):
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'amenity'
        name = Column(String(60))
    else:
        name = ""
