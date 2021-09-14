#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
    name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship('Place', secondary=place_amenity)
