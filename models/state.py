#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv
import models




class State(BaseModel, Base):
    """ State class """
    __tablename__= 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """lis of cities with satate_id equal to current id"""
            list_city = []
            dic_obj = models.storage.all(City)
            for city in list(dic_obj).values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
