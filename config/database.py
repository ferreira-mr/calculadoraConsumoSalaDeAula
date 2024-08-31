from peewee import SqliteDatabase

database = SqliteDatabase('database.db')


def startup_db():
    database.connect()

    from models.bandeira import BandeiraDB
    from models.comodo import ComodoDB
    from models.dispositivo import DispositivoDB
    from models.residencia import ResidenciaDB
    from models.tipo import TipoDB

    database.create_tables(
        [ResidenciaDB, BandeiraDB, ComodoDB, DispositivoDB, TipoDB]
    )


def shutdown_db():
    database.close()
