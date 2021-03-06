from abc import ABC

from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class DB(ABC):
    """Implements basic behavior of class interacts with sqlalchemy orm"""

    def __init__(self, db_session: sessionmaker):
        """Provide async-sessionmaker to class instance"""
        self._session: sessionmaker = db_session
