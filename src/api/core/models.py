from sqlalchemy import (
    Column, BigInteger, String, DateTime, Integer, Float, Date,
    Numeric, ForeignKeyConstraint, text
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)
    session_token = Column(String(255), nullable=True, unique=True)
    hash = Column(String(255), nullable=False)
    updated_on = Column(
        DateTime,
        nullable=False,
        server_default=text('CURRENT_TIMESTAMP'),
        server_onupdate=text('CURRENT_TIMESTAMP')
    )

    vehicle_ownerships = relationship('VehicleOwnership', back_populates='user')
    mpg_logs = relationship('MPGLog', back_populates='user')


class Vehicles(Base):
    __tablename__ = 'Vehicles'

    registration = Column(String(10), primary_key=True)
    updated_on = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    make = Column(String(50), nullable=True)
    year = Column(Integer, nullable=True)
    emissions = Column(Numeric(10, 0), nullable=True)
    colour = Column(String(30), nullable=True)

    vehicle_ownerships = relationship('VehicleOwnership', back_populates='vehicle')
    mpg_logs = relationship('MPGLog', back_populates='vehicle')


class VehicleOwnership(Base):
    __tablename__ = 'VehicleOwnership'

    registration = Column(String(10), primary_key=True)
    user_id = Column(BigInteger, primary_key=True)
    updated_on = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    __table_args__ = (
        ForeignKeyConstraint(
            ['registration'],
            ['Vehicles.registration'],
            name='vehicle_reg_ownership'
        ),
        ForeignKeyConstraint(
            ['user_id'],
            ['Users.id'],
            name='vehicle_owner'
        ),
    )

    vehicle = relationship('Vehicles', back_populates='vehicle_ownerships')
    user = relationship('Users', back_populates='vehicle_ownerships')


class MPGLog(Base):
    __tablename__ = 'MPGLog'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    registration = Column(String(10), nullable=False)
    mpg = Column(Float, nullable=False)
    litres = Column(Float, nullable=False)
    miles = Column(Float, nullable=False)
    total_cost = Column(Float, nullable=False)
    price_per_litre = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    created_on = Column(
        DateTime,
        nullable=True,
        server_default=text('CURRENT_TIMESTAMP'),
        server_onupdate=text('CURRENT_TIMESTAMP')
    )

    __table_args__ = (
        ForeignKeyConstraint(
            ['user_id'],
            ['Users.id'],
            name='mpglog_users_mapping'
        ),
        ForeignKeyConstraint(
            ['registration'],
            ['Vehicles.registration'],
            name='mpglog_vehicle_ownership'
        ),
    )

    user = relationship('Users', back_populates='mpg_logs')
    vehicle = relationship('Vehicles', back_populates='mpg_logs')
