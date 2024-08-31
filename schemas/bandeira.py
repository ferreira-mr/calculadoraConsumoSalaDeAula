from enum import Enum

from pydantic import BaseModel


class BandeiraCreate(BaseModel):
    tipo: int
    tarifa: float


class BandeiraRead(BaseModel):
    id: int
    tipo: int
    tarifa: float


class BandeiraUpdate(BaseModel):
    tarifa: float
