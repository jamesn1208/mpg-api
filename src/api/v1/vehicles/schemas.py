from pydantic import BaseModel


class Vehicle(BaseModel):
    id: int
    registration: str
    make: str
    emissions: float
    year: str
    colour: str


class AddVehicle(BaseModel):
    registration: str
