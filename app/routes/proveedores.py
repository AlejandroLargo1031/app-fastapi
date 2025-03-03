from fastapi import APIRouter, HTTPException
from app.models import Proveedor

router = APIRouter()

# Base de datos en memoria (Lista)
proveedores = [
    {"id": 1, "empresa": "Tech Distributors", "contacto": "Carlos López"},
    {"id": 2, "empresa": "Gadgets Supply", "contacto": "María Rodríguez"}
]

@router.get("/proveedores")
def get_proveedores():
    return proveedores

@router.post("/proveedores")
def add_proveedor(proveedor: Proveedor):
    if proveedor.id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")
    
    for item in proveedores:
        if item["id"] == proveedor.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    
    proveedores.append(proveedor.dict())
    return {"message": "Proveedor agregado", "data": proveedores}

@router.put("/proveedores/{id}")
def update_proveedor(id: int, proveedor: Proveedor):
    if id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")

    for index, item in enumerate(proveedores):
        if item["id"] == id:
            proveedores[index].update(proveedor.dict(exclude={"id"}))  
            return {"message": "Proveedor actualizado", "data": proveedores[index]}
    
    raise HTTPException(status_code=404, detail="Proveedor no encontrado")

@router.delete("/proveedores/{id}")
def delete_proveedor(id: int):
    if id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")

    for index, item in enumerate(proveedores):
        if item["id"] == id:
            proveedores.pop(index)
            return {"message": f"Proveedor con ID {id} eliminado"}
    
    raise HTTPException(status_code=404, detail="Proveedor no encontrado")