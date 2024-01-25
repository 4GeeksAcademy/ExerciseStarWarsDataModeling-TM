import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(35), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_planet = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    description = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    id_character = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'
    id_favorites = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id_planet'))
    planet = relationship(Planet)
    character_id = Column(Integer, ForeignKey('character.id_character'))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
