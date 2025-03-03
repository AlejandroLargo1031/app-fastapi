from pydantic import BaseModel

class Celular(BaseModel):
    id: int
    marca: str
    modelo: str
    precio: float

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str

class Proveedor(BaseModel):
    id: int
    empresa: str
    contacto: str
