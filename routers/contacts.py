from fastapi import APIRouter
from peewee import *
from database import db, cursor

router_contacts = APIRouter(
    prefix="/contacts",
    tags=["Contactos."]
)


@router_contacts.get("/", summary="List of contacts", description="Returns all contacts")
async def get_contacts():
    # create(first_name='Addu', last_name='Pagal', email='addu@gmail.com', phone='123-494', status=1)
    return [{'status': 'OK'}]


@router_contacts .get("/view/{id}", summary="Returns a single contact")
async def view(id: int):
    """ 
        Para ver todos los detalles relacionados con un solo contacto
- **id**: el número entero de identificación del contacto del que desea ver los detalles. 
    """
    return [{'estado': 'OK'}]
