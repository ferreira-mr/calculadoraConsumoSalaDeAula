from peewee import AutoField, FloatField, IntegerField, Model

from config.database import database


class BandeiraDB(Model):
    id = AutoField()
    tipo = IntegerField(choices=[1, 2, 3, 4])
    tarifa = FloatField()

    class Meta:
        database = database
