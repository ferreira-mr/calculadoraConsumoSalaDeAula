from peewee import AutoField, CharField, FloatField, Model

from config.database import database


class TipoDB(Model):
    id = AutoField()
    nome = CharField()
    valor_kwh = FloatField()

    class Meta:
        database = database
