import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    last_name_2 = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(12), nullable=False)
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name_planets = Column(String(30))
    users = relationship("users", backref="planets", lazy=True)
    fk_planets = Column(Integer, ForeignKey('users.id'))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name_characters = Column(String(30))
    user = relationship("user", backref="characters", lazy=True)
    fk_characters = Column(Integer, ForeignKey('users.id'))
    
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name_planets = Column(String(30))
    name_characters = Column(String(30))
    name_user = Column(String(30))    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')