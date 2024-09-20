#!/usr/bin/python3
"""Defines a new storage engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review


class DBStorage:
    """Represents our database storage engine"""

    __engine = None
    __session = None

    _class_mapping = {
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "User": User,
    }

    def __init__(self):
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}:{}:{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session(self.__session) all
        objects depending on te class name

        Args:
            cls (class, optional): _description_. Defaults to None.
        """
        objects = []
        if cls is None:
            for cls_type in DBStorage._class_mapping.values():
                objects.extend(self.__session.query(cls_type).all())
        else:
            if isinstance(cls, str):
                cls = DBStorage._class_mapping.get(cls)
                if cls is None:
                    raise ValueError(f"Class {cls} not found in mapping")
                objects = self.__session.query(cls).all()
        return {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objects}


def new(self, obj):
    """Add the object to the current database session

    Args:
        obj (object):an instance of a class
    """
    self.__session.add(obj)


def save(self):
    """Commit all changes of the current database session"""
    self.__session.commit()


def delete(self, obj=None):
    """Deletes from the current database session obj if not None.

    Args:
        obj (object, optional): _description_. Defaults to None.
    """
    if obj:
        self.__session.delete(obj)


def reload(self):
    """Create all tables in the databases."""
    Base.metadata.create_all(self.__engine)
    session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
    Session = scoped_session(session_factory)
    self.__session = Session()
