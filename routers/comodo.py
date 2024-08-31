from fastapi import APIRouter

from models.comodo import ComodoDB
from schemas.comodos import ComodoCreate, ComodoRead, ComodoUpdate

router = APIRouter(prefix='/comodos', tags=['CÔMODOS'])


@router.post(path='', response_model=ComodoRead)
def criar_comdo(novo_comodo: ComodoCreate):
    comodo = ComodoDB.create(**novo_comodo.model_dump())
    return comodo


@router.get(path='', response_model=list[ComodoRead])
def lista_residncias():
    residencias = ComodoDB.select()
    return residencias


@router.get(path='/{id}', response_model=ComodoRead)
def lista_residencia(id):
    residencia = ComodoDB.get_or_none(ComodoDB.id == id)
    return residencia


@router.patch(path='/{id}', response_model=ComodoRead)
def update_residencia(id, novo_comodo: ComodoUpdate):
    residencia = ComodoDB.get_or_none(ComodoDB.id == id)
    residencia.nome = novo_comodo.nome
    residencia.save()
    return residencia


@router.delete(path='/{id}', response_model=ComodoRead)
def delete_residencia(id):
    residencia = ComodoDB.get_or_none(ComodoDB.id == id)
    residencia.delete_instance()
    return residencia
