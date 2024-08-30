from fastapi import APIRouter


from schemas.dispositivos import DispositivoRead, DispositivoCreate, DispositivoUpdate
from models.dispositivo import DispositivoDB


router = APIRouter(prefix="/dispositivos", tags=["DISPOSITIVOS"])

@router.post("/", response_model=DispositivoRead)
def criar_dispositivo(novo_dispositivo: DispositivoCreate):
    dispositivo = DispositivoDB(**novo_dispositivo.model_dump())
    return dispositivo

@router.get("/", response_model=list[DispositivoRead])
def listar_dispositivos():
    dispositivos = DispositivoDB.select()
    return dispositivos

@router.get("/{id}", response_model=DispositivoRead)
def listar_dispositivo(id: int):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == id)
    return dispositivo

@router.put("/{id}", response_model=DispositivoRead)
def atualizar_dispositivo(id: int, dispositivo_autualizado: DispositivoUpdate):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == id)
    dispositivo.nome = dispositivo_autualizado.nome
    dispositivo.consumo = dispositivo_autualizado.consumo
    dispositivo.uso_diario = dispositivo_autualizado.uso_diario
    dispositivo.save()
    return dispositivo

@router.delete("/{id}", response_model=DispositivoRead)
def eliminar_dispositivo(id: int):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == id)
    dispositivo.delete_instance()
    return dispositivo


