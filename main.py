from fastapi import FastAPI
from routes.data_potensi import dapot

app = FastAPI(
    title='Dira Abinawa - Data Potensi',
    version='1.0.0'
)
app.include_router(dapot)