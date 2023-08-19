from pydantic import BaseModel


class Producto(BaseModel):
    id: int
    sku : str
    bienes_transp : str
    descripcion : str
    unidad : str
    peso : float
