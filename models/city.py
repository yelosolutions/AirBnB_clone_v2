#!/usr/bin/python3
""" This is the city class """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The is the class for city
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade='all, delete, delete-orphan')
