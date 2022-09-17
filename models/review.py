#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String


class Review(BaseModel, Base):
    """Represents a review for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table reviews.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Reviews.
        text (sqlalchemy String): The review description.
        place_id (sqlalchemy String): The review's place id.
        user_id (sqlalchemy String): The review's user id.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
=======
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """This is the class for Review
    Inherits from SQLAlchemy Base and links to the MySQL table reviews.
    Attributes:
        place_id: (sqlalchemy String): The review's place id.
        user_id: (sqlalchemy String): The review's place id.)
        text: (sqlalchemy String): The review description
    """

    __tablename__ = "reviews"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
>>>>>>> 39580ecaddb8895577e5e1b577d27e7c2e03ed0f
