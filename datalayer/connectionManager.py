from typing import Union

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

        return scoped_session(sessionmaker(bind=self._engine))

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

    def init(self, base=None, engine=None):
        """docstring for init"""
        if not engine and not self._engine:
            print('INITIALIZING ERROR: no engine provided nor found')
            return False
        if base:
            self._base = base

        if engine:
            self._engine = engine

        self._base.metadata.create_all(bind=self._engine)
