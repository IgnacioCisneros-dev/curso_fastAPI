from fastapi import APIRouter
from service.producto_service import buscar_producto_por_id, buscar_productos, guardar_nuevo_producto
from service.producto_service import actualizar_producto
from models.Productos import Producto

router_productos = APIRouter(prefix="/productos",
                             tags=["Productos."])


@router_productos.get("/obtener",
                      summary='Lista de productos.',
                      description='Recupera una lista de productos de la base de datos.')
async def obtener_productos():
    print('OK')
    resultado = await buscar_productos()
    return resultado


@router_productos.get("/{producto_id}",
                      summary='Obtiene un producto po ID',
                      description='Busca en base de datos un producto por el id que se le pasa como parametro.')
async def obtener_producto_por_id(producto_id: int):
    producto = await buscar_producto_por_id(producto_id)
    return producto


@router_productos.post("/guardar",
                       summary="Guarda un nuevo producto.",
                       description="Guarda un nuevo producto en base de datos.")
def guardar_producto(producto: Producto):
    return guardar_nuevo_producto(producto)


@router_productos.put("/editar/{producto_id}",
                      summary="endPoint que edita un producto.",
                      description="Edita un producto y se vuelve a guardar en base de datos.")
async def editar_producto(producto: Producto, producto_id: int):
    resultado = actualizar_producto(producto, producto_id)
    return resultado