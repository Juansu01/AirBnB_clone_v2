#!/usr/bin/python3
"""define DBStorage engine"""

from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base


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

        if cls is None:
