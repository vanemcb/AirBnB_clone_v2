#!/usr/bin/python3
""" Place Module for HBNB project """
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship(
        "Review", backref="place", cascade="all, delete", passive_deletes=True)

    @property
    def reviews(self):
        """ getter reviews """
        from models import storage
        dict_reviews = storage.all(Review)

        list_reviews = []
        for value in dict_reviews.values():
            dict_review = value.to_dict()

            if self.id == dict_review['place_id']:
                # Para guardar los diccionarios en lugar de los objetos cambiar
                # list_reviews.append(value) => list_reviews.append(dict_city)
                list_reviews.append(value)

        return list_reviews
