from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

# using 'abstract pattern' to allow different DeclarativeBase abstraction
# therefore making possible to use different Base implementation for
# different engines
# for DeclarativeBase mapping useful documentation see:
# https://docs.sqlalchemy.org/en/20/orm/declarative_config.html#other-declarative-mapping-directives


class Base(DeclarativeBase):
    """DeclarativeBase subclass"""


class DefaultAbstractBase(Base):
    """DefaultBase class to extend sqlalchemy DeclarativeBase"""
    __abstract__ = True
    metadata = MetaData()


if __name__ == "__main__":
    DefaultAbstractBase()
