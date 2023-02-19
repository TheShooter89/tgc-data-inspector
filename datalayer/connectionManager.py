import functools
from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker, SessionTransaction

from datalayer.customBase import DefaultAbstractBase


class ConnectionManager():
    """docstring for ConnectionManager"""
    _base = DefaultAbstractBase
    _engine = None
    _session = None

    def __init__(self, base=None, engine=None):
        if base:
            self._base = base
        if engine:
            self._engine = engine

    def _scoped_session_factory(self):
        """docstring for _create_scoped_session_factory"""
        if not self._engine:
            print('SCOPED SESSION FACTORY ERROR: no engine found')
            return False

        return scoped_session(sessionmaker(bind=self._engine, future=True))

    def _create_session(self):
        """docstring for _create_session"""
        if self._session:
            print('SESSION CREATION FAILURE: an active session already exists')
            return False

        self._session = self._scoped_session_factory()
        return self._session

    def _remove_session(self):
        """docstring for _create_session"""
        if not self._session:
            print('SESSION REMOVING FAILURE: no active session found')
            return False

        # self._session.remove()
        self._session = None
        return True

    def _load_engine(self, engine_string):
        """docstring for _load_engine"""
        if self._engine:
            print('an engine is already in use, returning self._engine')
            return self._engine
        self._engine = create_engine(engine_string)
        return self._engine

    def init(self, base=None, engine=None):
        """docstring for init"""
        if not engine and not self._engine:
            print('INITIALIZING ERROR: no engine provided nor found')
            return False
        if base:
            self._base = base

        if engine:
            self._engine = engine

        self._load_engine('default')
        self._base.metadata.create_all(bind=self._engine)

    def use_session(self, func):
        """docstring for use_session"""
        if not self._session:
            self._create_session()

        with self._session() as session:
            with session.begin():
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    value = func(session=self._session, *args, **kwargs)
                    return value

                return wrapper
