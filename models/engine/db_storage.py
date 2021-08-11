#!/usr/bin/python3
"""
    Database Engine Module
"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.log import instance_logger
from sqlalchemy.orm import Session
from sqlalchemy.orm.session import sessionmaker

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


instance = DBStorage()
