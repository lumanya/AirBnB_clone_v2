#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
            __tablename__ = 'user'
            first_name = Column(String(60))
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
