from fastapi import APIRouter

from models.tipo import TipoDB
from schemas.tipo import TipoCreate, TipoRead, TipoUpdate

router = APIRouter(prefix='/tipos', tags=['TIPOS'])


@router.post(path='', response_model=TipoRead)
def criar_tipo(novo_tipo: TipoCreate):
    tipo = TipoDB.create(**novo_tipo.model_dump())
    return tipo


@router.get(path='', response_model=list[TipoRead])
def listar_tipos():
    tipos = TipoDB.select()
    return tipos


@router.get(path='/{tipo_id}', response_model=TipoRead)
def listar_tipo(tipo_id):
    tipo = TipoDB.get_or_none(TipoDB.id == tipo_id)
    return tipo


@router.patch(path='/{tipo_id}', response_model=TipoRead)
def atualizar_tipo(tipo_id, tipo_atualizado: TipoUpdate):
    tipo = TipoDB.get_or_none(TipoDB.id == tipo_id)
    tipo.nome = tipo_atualizado.nome
    tipo.valor_kwh = tipo_atualizado.valor_kwh
    tipo.save()
    return tipo


@router.delete(path='/{tipo_id}', response_model=TipoRead)
def excluir_tipo(tipo_id):
    tipo = TipoDB.get_or_none(TipoDB.id == tipo_id)
    tipo.delete_instance()
    return tipo
