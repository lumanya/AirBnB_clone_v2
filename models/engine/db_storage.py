#!/usr/bin/python3
""" db_storage module that contains db_storage file"""

import os
from sqlalchemy import create_engine
from models.base_model import Base
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review 
from models.state import State
from sqlalchemy.orm import sessionmaker

classes = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """ db storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate clss"""
        db_user = os.getenv('HBNB_MYSQL_USER')
        db_pwd = os.getenv('HBNB_MYSQL_PWD')
        db_host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        db_url = 'mysql+mysqldb://db_user:db_pwd@db_host/db'
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session all obejts depending on class name"""
        dictionary = {}
        if cls:
            for obj in self.__session.query(cls).fetch_all():
                key = cls + obj.id
                value = obj
                dictionary[key] = value
                return dictionary
        else:
            pass
        