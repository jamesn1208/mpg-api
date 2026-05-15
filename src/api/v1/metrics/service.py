from sqlalchemy.orm import Session
from sqlalchemy import select

from api.core.models import MPGLog


async def get_metrics(session: Session) -> list[MPGLog]:
    return list(session.execute(select(MPGLog)).scalars())
