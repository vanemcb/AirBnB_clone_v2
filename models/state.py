#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref="state", cascade="all, delete", passive_deletes=True)

    @property
    def cities(self):
        """ getter cities """
        from models import storage
        dict_cities = storage.all(City)

        list_cities = []
        for value in dict_cities.values():
            dict_city = value.to_dict()

            if self.id == dict_city['state_id']:
                # Para guardar los diccionarios en lugar de los objetos cambiar
                # list_cities.append(value) => list_cities.append(dict_city)
                list_cities.append(value)

        return list_cities
        # name = ""
