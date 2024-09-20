#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Returns the list of city instances with state_id 
            """
            from models import storage
            from models.city import City
            city_inst = storage.all(City)
            city_list = list()
            for key, obj in city_inst.items():
                if self.id == obj.state_id:
                    city_list.append(obj)
            return city_list
