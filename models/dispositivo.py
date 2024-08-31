from peewee import AutoField, CharField, DoubleField, ForeignKeyField, Model

from config.database import database
from models.comodo import ComodoDB
from models.residencia import ResidenciaDB


class DispositivoDB(Model):
    id = AutoField()
    nome = CharField()
    consumo = DoubleField()
    uso_diario = DoubleField()
    comodo = ForeignKeyField(ComodoDB, backref='dispositivos')
    residencia = ForeignKeyField(ResidenciaDB, backref='dispositivos')

    class Meta:
        database = database
