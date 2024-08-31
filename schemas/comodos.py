from pydantic import BaseModel

from schemas.dispositivos import DispositivoRead


class ComodoCreate(BaseModel):
    nome: str
    residencia_id: int


class ComodoUpdate(BaseModel):
    nome: str


class ComodoRead(BaseModel):
    id: int
    nome: str
    residencia_id: int
    dispositivos: list[DispositivoRead] = []

    class Config:
        from_attributes = True
