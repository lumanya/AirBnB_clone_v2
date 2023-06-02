#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from os import getenv

class Place(BaseModel, Base):
    """ A place to stay """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'place'
        # city_id = ""
        # user_id = ""
        name = Column(String(60), nullable=False)
        # description = ""
        # number_rooms = 0
        # number_bathrooms = 0
        # max_guest = 0
        # price_by_night = 0
        # latitude = 0.0
        # longitude = 0.0
        # amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = Column(String(60), nullable=False)
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []


