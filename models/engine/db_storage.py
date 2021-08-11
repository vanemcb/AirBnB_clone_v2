#!/usr/bin/python3
"""
    Database Engine Module
"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.log import instance_logger
from sqlalchemy.orm import Session, query, scoped_session
from sqlalchemy.orm.session import sessionmaker


os.environ.update({
    "HBNB_ENV": "dev",
    "HBNB_MYSQL_USER": "hbnb_dev",
    "HBNB_MYSQL_PWD": "hbnb_dev_pwd",
    "HBNB_MYSQL_HOST": "localhost",
    "HBNB_MYSQL_DB": "hbnb_dev_db"
})

HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST")
HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")


class DBStorage:
    """
        DBStorage class definition
    """

    __engine = None
    __session = None

    def __init__(self):
        """ Intance Method """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB), pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            meta = MetaData(self.__engine)
            meta.reflect()
            meta.drop_all()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {'State': State, 'City': City}

        query_dict = {}

        if cls is None:
            for value in classes.values():
                for obj in self.__session.query(value).all():
                    query_dict.update(
                        {obj.__class__.__name__ + "." + obj.id: obj})
        else:
            for obj in self.__session.query(cls).all():
                query_dict.update(
                    {obj.__class__.__name__ + "." + obj.id: obj})

        self.__session.close()
        return query_dict

    def new(self, obj):
        """Method that adds the object to the current database session"""
        self.__session.add(obj)
        self.__session.close()

    def save(self):
        """ Method that commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Method that delete from the current database session
        obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Method that creates all tables in the database """
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
