from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from app.routes import celulares, clientes, proveedores 
from fastapi.staticfiles import StaticFiles



app = FastAPI()

# Asegurar que la carpeta templates existe
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
if not os.path.exists(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR)

# Configurar Jinja2 para renderizar HTML
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# 🔹 REGISTRAR LAS RUTAS DEL CRUD
app.include_router(celulares.router, prefix="/api", tags=["Celulares"])
app.include_router(clientes.router, prefix="/api", tags=["Clientes"])
app.include_router(proveedores.router, prefix="/api", tags=["Proveedores"])

app.mount("/static", StaticFiles(directory="static"), name="static")
# Ruta principal
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
