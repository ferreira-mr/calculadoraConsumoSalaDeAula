from fastapi import APIRouter

from models.residencia import ResidenciaDB
from schemas.residencias import (ResidenciaCreate, ResidenciaRead,
                                 ResidenciaUpdate)

router = APIRouter(prefix='/residencias', tags=['RESIDÊNCIAS'])


@router.post('')
def criar_residencia(novo_residencia: ResidenciaCreate):
    residencia = ResidenciaDB.create(**novo_residencia.model_dump())

    return residencia


@router.get(path='', response_model=list[ResidenciaRead])
def listar_residencias():
    residencias = ResidenciaDB.select()
    return residencias


@router.get(path='/{id}', response_model=ResidenciaRead)
def listar_residencia(id):
    residencia = ResidenciaDB.get_or_none(ResidenciaDB.id == id)
    return residencia


@router.patch(path='/{id}', response_model=ResidenciaRead)
def atualizar_residencia(id, residencia_atualizada: ResidenciaUpdate):
    residencia = ResidenciaDB.get(ResidenciaDB.id == id)
    residencia.proprietario = residencia_atualizada.proprietario
    residencia.save()
    return residencia


@router.delete(path='/{id}')
def eliminar_residencia(id):
    residencia = ResidenciaDB.get(ResidenciaDB.id == id)
    residencia.delete_instance()
    return residencia
