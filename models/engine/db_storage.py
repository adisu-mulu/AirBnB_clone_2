#!/usr/bin/python3
""" This module represents the db_storage """
import os
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.base_model import BaseModel
from sqlalchemy import (create_engine)
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True)
                                      )
        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData(bind=self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """   """
        objects = {}
        if cls:
            classes = {'Amenity': Amenity, 'City': City, 'Place': Place,
                       'State': State, 'Review': Review, 'User': User}
            results = self.__session.query(classes[cls]).all()
            for instance in results:
                objects.update({instance.__class__.__name__ +
                                '.' + instance.id: instance})
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for clss in classes:
                results = self.__session.query(clss).all()
                for instance in results:
                    objects.update({instance.__class__.__name__ +
                                    '.' + instance.id: instance.to_dict()})
        return objects

    def new(self, obj):
        """ adding object to current session"""
        self.__session.add(obj)

    def save(self):
        """ commiting the current session """
        self.__session.commit()

    def delete(self, obj=None):
        """ deleting object from session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """close method"""
        if self.__session:
            self.__session.remove()
