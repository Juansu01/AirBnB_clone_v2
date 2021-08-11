#!/usr/bin/python3
"""define DBStorage engine"""

from sqlalchemy import create_engine
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.orm import query
from models.base_model import Base, BaseModel




class DBStorage:
    """DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        passw = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                    .format(user, passw, host, db),
                                     pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all object of given class"""
        dictionary = {}

        if cls is None:

            _query = self.__session.query(User, State, City, Amenity,
                                      Place, Review)
            for obj in _query:
                key_obj = ("{}.{}".format(type(obj).__name__, obj.id))
                dictionary[key_obj] = obj
            return dictionary
        else:
            if type(cls) == str:
                cls = eval(cls)
            _query = self.__session.query(cls)
            for obj in _query:
                key_obj = ("{}.{}".format(type(obj).__name__, obj.id))
                dictionary[key_obj] = obj
            return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""


    def delete(self, obj=None):
        """delete from the current database session, obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Created all tables in the database"""
        Base.metadata.create_all(self.__engine)

        Session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_factory)
        self.__session = Session()

