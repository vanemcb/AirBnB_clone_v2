#!/usr/bin/python3
"""
    Database Engine Module
"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.log import instance_logger
from sqlalchemy.orm import Session, query
from sqlalchemy.orm.session import sessionmaker
# from models import user, state, city, amenity, place, review

# os.environ[env_var] = env_var_value

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

# classes = [user.User]
# print(classes[0].__name__)


class DBStorage:
    """
        DBStorage class definition
    """

    __engine = None
    __session = None

    def __init__(self):
        """ Pass """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            # Session = sessionmaker(self.__engine)
            # session = Session()
            ##################
            meta = MetaData(self.__engine)
            meta.reflect()
            meta.drop_all()

    def all(self, cls=None):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        self.__session = Session(self.__engine)
        list_objects = self.__session.query(cls).all()
        query_dict = {}
        for obj in list_objects:
            query_dict.update({str(cls.__name__) + "." + obj.id: obj})
        return query_dict


instance = DBStorage()
instance.all()
