from peewee import AutoField, CharField, DoubleField, ForeignKeyField, Model

from config.database import database
from models.dependencia import DependenciaDB
from models.tipo_dispositivo import TipoDispositivoDB
from models.unidade_consumidora import UnidadeConsumidoraDB


class DispositivoDB(Model):
    id = AutoField()
    nome = CharField()
    consumo = DoubleField()
    uso_diario = DoubleField()
    tipo = ForeignKeyField(TipoDispositivoDB, backref='dispositivos')
    dependencia = ForeignKeyField(DependenciaDB, backref='dispositivos')
    unidade_consumidora = ForeignKeyField(
        UnidadeConsumidoraDB, backref='dispositivos'
    )

    class Meta:
        database = database
