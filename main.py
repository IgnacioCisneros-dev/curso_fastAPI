from fastapi import FastAPI
from routers import contacts, productos

app = FastAPI(title='Ejemplo CRUD basico.',
              description='Ejemplo de un CRUD basico conectado a una BD MySQL local.', version='0.0.1')
app.include_router(productos.router_productos)
