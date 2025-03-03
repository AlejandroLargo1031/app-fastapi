from fastapi import APIRouter, HTTPException
from app.models import Cliente

router = APIRouter()

# Base de datos en memoria (Lista)
clientes = [
    {"id": 1, "nombre": "Juan largo", "email": "juanlargo@example.com"},
    {"id": 2, "nombre": "alejandro largo", "email": "alejandro@example.com"}
]

@router.get("/clientes")
def get_clientes():
    return clientes

@router.post("/clientes")
def add_cliente(cliente: Cliente):
    if cliente.id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")
    
    for item in clientes:
        if item["id"] == cliente.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    
    clientes.append(cliente.dict())
    return{'message': "Cliente agregado", 'data':clientes}


@router.put("/clientes/{id}")
def update_cliente(id: int, cliente: Cliente):
    if id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")

    for index, item in enumerate(clientes):
        if item["id"] == id:
            clientes[index].update(cliente.dict(exclude={"id"})) 
            return {"message": "Cliente actualizado", "data": clientes[index]}
    
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@router.delete("/clientes/{id}")
def delete_cliente(id: int):
    if id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")

    for index, item in enumerate(clientes):
        if item["id"] == id:
            clientes.pop(index)
            return {"message": f"Cliente con ID {id} eliminado"}
    
    raise HTTPException(status_code=404, detail="Cliente no encontrado")