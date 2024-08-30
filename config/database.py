from peewee import  SqliteDatabase

database = SqliteDatabase('database.db')

def startup_db():
    from models.residencia import ResidenciaDB
    database.connect()
    database.create_tables([ResidenciaDB])

def shutdown_db():
    database.close()

