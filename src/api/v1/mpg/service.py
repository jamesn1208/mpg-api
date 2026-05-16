import logging

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from asyncio import to_thread

from api.core.schemas import ActionResponse
from api.core.exceptions import ActionError
from . import schemas, models


async def log_mpg(log: schemas.MPGLog, session: Session, user_id: int) -> ActionResponse:
    if not await to_thread(models.is_vehicle_registered_to_user,
                           registration=log.registration,
                           session=session,
                           user_id=user_id):
        raise ActionError(status_code=400,
                          message="The provided vehicle registration is not registered to you.")

    try:
        await to_thread(models.insert_mpg_log,
                        log=log,
                        session=session,
                        user_id=user_id)
    except IntegrityError:
        logging.exception("Got IntegrityError whilst inserting log data into database.")
        raise ActionError(status_code=500,
                          message="Failed to insert MPG log data.")

    return ActionResponse(success=True,
                          message="Successfully inserted MPG log data.")


async def get_mpg_history(limit: int, offset: int, session: Session, user_id: int) -> list[schemas.MPGLog]:
    pass
