from contextlib import asynccontextmanager
from uvicorn import run
from fastapi import FastAPI
from os import environ
from toml import loads
from sys import stdout
import logging

from api.core.router import router
from api.core import config, models, handlers


logging.basicConfig(level=config.LOGGING_LEVEL,
                    format=config.LOGGING_FORMAT,
                    stream=stdout)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.database = config.get_session_maker()
    engine = app.state.database.kw["bind"]
    if engine is None:
        raise RuntimeError("Database engine is not configured properly.")
    models.Base.metadata.create_all(engine)

    yield

    app.state.database.kw["bind"].dispose()
    del app.state.database


pyproject = loads(open(f"{environ['WORKDIR']}/pyproject.toml").read())
APP = FastAPI(
    title="Fuel API",
    description=pyproject['project']['description'],
    version=pyproject['project']['version'],
    lifespan=lifespan,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

handlers.register(APP)
APP.include_router(router)

if __name__ == "__main__":
    run("api.main:APP",
        host=config.API_HOST,
        port=config.API_PORT)
