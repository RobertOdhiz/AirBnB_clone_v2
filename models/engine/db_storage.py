#!/usr/bin/python3
"""DB storage
"""
import models
from models.base_model import BaseModel, Base
from models import city, state
from os import environ, getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DBStorage:
    """database storage for mysql conversion
    """
    __engine = None
    __session = None

    def __init__(self):
        """initializer for DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database =  getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, pwd, host, database),
                                      pool_pre_ping=True)
        env = getenv('HBNB_ENV')
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session """
        objects = {}
        if cls:
            if type(cls) == str:
                cls = dummy_classes[cls]
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """ adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current db session """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes from the current db session """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """ creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
