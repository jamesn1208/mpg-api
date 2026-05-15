from contextlib import asynccontextmanager
from uvicorn import run
from fastapi import FastAPI
from os import environ
from toml import loads


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Hello from fuel-api!")

    yield


pyproject = loads(open(f"{environ['WORKDIR']}/pyproject.toml").read())
app = FastAPI(
    title="Fuel API",
    description=pyproject['project']['description'],
    version=pyproject['project']['version'],
    lifespan=lifespan
)

if __name__ == "__main__":
    run(host="0.0.0.0",
        port=8080,
        app=app)
