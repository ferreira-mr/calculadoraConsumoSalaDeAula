from pydantic import BaseModel


class TipoCreate(BaseModel):
    nome: str
    valor_kwh: float


class TipoUpdate(BaseModel):
    nome: str
    valor_kwh: float


class TipoRead(BaseModel):
    id: int
    nome: str
    valor_kwh: float
