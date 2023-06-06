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
from sqlalchemy.orm import sessionmaker, scoped_session


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
        db_url = f'mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db}'
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session all obejts
        depending on class name"""
        if self.__session:
            self.reload()
        objects = {}
        if type(cls) == str:
            cls = classes.get(cls, None)
        if cls:
            for obj in self.__session.query(cls):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in classes.values():
                for obj in self.__session.query(cls):
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return objects

    def new(self, obj):
        """create a new objects"""
        self.__session.add(obj)

    def save(self):
        """commit al changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from current database session """
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads objects from the dtabase"""
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Dispose of current session if active"""
        self.__session.remove()
