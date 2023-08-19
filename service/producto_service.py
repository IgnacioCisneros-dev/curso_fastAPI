from fastapi import APIRouter
from database import db, cursor
from models.Productos import Producto


async def buscar_productos():
    """Funcion que obtiene todos los productos de la base de datos.

    Returns:
        Diccionario: Retorna un diccionario de todos los productos existentes en la base de datos.
    """
    consulta = "SELECT * FROM cat_productos"
    cursor.execute(consulta)
    # productos = Producto()
    productos = cursor.fetchall()

    lista_productos = []

    for item in productos:
        producto = Producto(
            id=item[0],
            sku=item[1],
            bienes_transp=item[2],
            descripcion=item[3],
            unidad=item[4],
            peso=item[5]
        )
        lista_productos.append(producto)
    return lista_productos


async def buscar_producto_por_id(producto_id: int):
    """Funcion que busca un producto por el id

    Args:
        producto_id (int): Id del producto que se desea buscar

    Returns:
        Producto: producto
    """
    consulta = "SELECT * FROM cat_productos WHERE id = %s"
    cursor.execute(consulta, (producto_id,))
    producto = cursor.fetchall()
    return {"Producto: ": producto}


def guardar_nuevo_producto(producto: Producto):
    """Funcion que guarda un nuevo producto en base de datos.

    Args:
        producto (Producto): Producto que persiste en base de datos.

    Returns:
        String: Muestra un mensaje que indica que el producto fue guardado.
    """

    insert = "INSERT INTO cat_productos (sku,bienes_transp, descripcion, unidad, peso) VALUES (%s, %s, %s, %s, %s)"
    valores = (producto.sku,
               producto.bienes_transp,
               producto.descripcion,
               producto.unidad,
               producto.peso)

    cursor.execute(insert, valores)
    db.commit()

    return 'Producto guardado correctamente.'


def actualizar_producto(producto_actualizar: Producto, producto_id: int):
    """Funcion que sirve para poder editar un producto.

    Args:
        producto_actualizar (Producto): Informacion del producto que se va a editar.
        producto_id (int): id de producto que se va a editar

    Returns:
        String : Mensaje que indica que el producto se actualizo correctamente.
    """

    update = 'UPDATE cat_productos SET sku=%s, bienes_transp=%s, descripcion=%s, unidad=%s, peso=%s WHERE id=%s'
    valores = (producto_actualizar.sku,
              producto_actualizar.bienes_transp,
             producto_actualizar.descripcion,
           producto_actualizar.unidad,
          producto_actualizar.peso,
         producto_id)

    cursor.execute(update, valores)
    db.commit()

    return 'Producto actualizado correctamente.'
