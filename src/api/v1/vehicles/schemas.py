from pydantic import BaseModel


class Vehicle(BaseModel):
    id: int
    registration: str
    make: str
    emissions: float
    year: int
    colour: str


class AddVehicle(BaseModel):
    registration: str
    make: str
    emissions: float
    year: int
    colour: str


class CheckVehicle(BaseModel):
    registration: str
