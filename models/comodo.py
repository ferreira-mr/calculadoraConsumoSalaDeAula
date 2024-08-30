from peewee import AutoField, CharField, ForeignKeyField, Model
from config.database import database
from models.residencia import ResidenciaDB

class ComodoDB(Model):
    id = AutoField()
    nome = CharField()
    residencia = ForeignKeyField(ResidenciaDB, backref='comodos')

    class Meta:
        database = database