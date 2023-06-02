#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from os import getenv


class Review(BaseModel, Base):
    """ Review classto store review information """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'review'
        text = Column(String(120))
    else:
        place_id = ""
        user_id = ""
        text = ""
