from fastapi import APIRouter

from schemas.comodos import ComodoCreate, ComodoUpdate, ComodoRead
from models.comodo import ComodoDB

router = APIRouter(prefix="/comodos", tags=["CÔMODOS"])

@router.post('/', response_model=ComodoRead)
def criar_comdo(novo_comodo: ComodoCreate):
    comodo = ComodoDB(**novo_comodo.model_dump())
    return comodo

@router.get('/', response_model=list[ComodoRead])
def lista_residncias():
    residencias = ComodoDB.select()
    return residencias

@router.get('/{id}', response_model=ComodoRead)
def lista_residencia(id):
    residencia = ComodoDB.get_or_none(ComodoDB.id == id)
    return residencia

@router.put('/{id}', response_model=ComodoRead)
def update_residencia(id, novo_comodo: ComodoUpdate):
    residencia = ComodoDB.get_or_none(ComodoDB.id == id)
    residencia.nome = novo_comodo.nome
    residencia.save()
    return residencia

@router.delete('/{id}', response_model=ComodoRead)
def delete_residencia(id):
    residencia = ComodoDB.get_or_none(ComodoDB.id == id)
    residencia.delete_instance()
    return residencia




