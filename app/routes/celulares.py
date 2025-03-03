from fastapi import APIRouter, HTTPException
from app.models import Celular

router = APIRouter()

# Datos iniciales con IDs únicos
celulares = [
    {"id": 1, "marca": "Samsung", "modelo": "Galaxy S23", "precio": 200},
    {"id": 2, "marca": "Apple", "modelo": "iPhone 14", "precio": 150}
]

@router.get("/celulares")
def get_celulares():
    return celulares

@router.post("/celulares")
def add_celular(celular: Celular):
    if celular.id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")
    
    for item in celulares:
        if item["id"] == celular.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    
    celulares.append(celular.dict())
    return {"message": "Celular agregado", "data": celulares}

@router.put("/celulares/{id}")
def update_celular(id: int, celular: Celular):
    if id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")

    for index, item in enumerate(celulares):
        if item["id"] == id:
            celulares[index].update(celular.dict(exclude={"id"})) 
            return {"message": "Celular actualizado", "data": celulares[index]}
    
    raise HTTPException(status_code=404, detail="Celular no encontrado")

@router.delete("/celulares/{id}")
def delete_celular(id: int):
    if id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")

    for index, item in enumerate(celulares):
        if item["id"] == id:
            celulares.pop(index)
            return {"message": f"Celular con ID {id} eliminado"}
    
    raise HTTPException(status_code=404, detail="Celular no encontrado")
