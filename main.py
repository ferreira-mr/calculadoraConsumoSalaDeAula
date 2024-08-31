from fastapi import FastAPI

from config.database import shutdown_db, startup_db
from routers.bandeira import router as bandeira_router
from routers.comodo import router as comodo_router
from routers.dispositivo import router as dispositivos_router
from routers.residencia import router as residencia_router
from routers.tipo import router as tipo_router

app = FastAPI()

app.include_router(residencia_router)
app.include_router(comodo_router)
app.include_router(dispositivos_router)
app.include_router(bandeira_router)
app.include_router(tipo_router)

app.add_event_handler('startup', startup_db)
app.add_event_handler('shutdown', shutdown_db)
