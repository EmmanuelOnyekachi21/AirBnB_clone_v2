#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref='state', cascade='all, delete'
    )
    
    @property
    def cities(self):
        """Property decorator for cities attribute
        """
        from models.city import City
        # Get all cities from storage
        all_cities = storage.all(City)
        # Initialize a list to store the cities for the state
        state_cities = []
        
        for city in all_cities.values():
            if city.state_id == self.id:
                state_cities.append(city)

        return state_cities
