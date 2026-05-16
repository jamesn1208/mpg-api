from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from datetime import datetime

from api.core.models import MPGLog, VehicleOwnership
from . import schemas


def is_vehicle_registered_to_user(registration: str, user_id: int, session: Session) -> bool:
    """
    Check if the vehicle provided is registered to the user.

    :param registration: The vehicle registration number to check.
    :param user_id: The user_id to check against.
    :param session: The database session to use.
    :return: True if the vehicle is registered to the user, False otherwise.
    """
    try:
        (session.execute(
            select(VehicleOwnership)
            .where(
                VehicleOwnership.user_id == user_id,  # type: ignore
                VehicleOwnership.registration == registration))  # type: ignore
         .one())
    except NoResultFound:
        return False
    return True


def insert_mpg_log(log: schemas.MPGLog,
                   session: Session,
                   user_id: int) -> None:
    """
    Insert a new MPG log entry into the database.

    :param log: MPGLog schema containing new log data.
    :param session: The database session to use.
    :param user_id: The user_id to associate with the entry.
    :return: Nothing.
    """
    log_entry = MPGLog(user_id=user_id,
                       registration=log.registration,
                       mpg=log.mpg,
                       litres=log.litres,
                       miles=log.miles,
                       total_cost=log.total_cost,
                       price_per_litre=round((log.total_cost * 100) / log.litres, 1),
                       date=datetime.strptime(log.date, "%Y-%m-%d"))
    session.add(log_entry)
    session.flush()
