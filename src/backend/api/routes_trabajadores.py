from fastapi import APIRouter, HTTPException
from models import Trabajador

router = APIRouter()

trabajadores_db = []

@router.post("/")
def crear_trabajador(trabajador: Trabajador):
    for t in trabajadores_db:
        if t["id"] == trabajador.id:
            raise HTTPException(status_code=400, detail="Trabajador ya existe")
    trabajadores_db.append(trabajador.model_dump())
    return trabajador

@router.get("/")
def listar_trabajadores():
    return trabajadores_db

@router.get("/{trabajador_id}")
def obtener_trabajador(trabajador_id: int):
    for t in trabajadores_db:
        if t["id"] == trabajador_id:
            return t
    raise HTTPException(status_code=404, detail="Trabajador no encontrado")

@router.put("/{trabajador_id}/desactivar")
def desactivar_trabajador(trabajador_id: int):
    for t in trabajadores_db:
        if t["id"] == trabajador_id:
            t["activo"] = False
            return t
    raise HTTPException(status_code=404, detail="Trabajador no encontrado")
