from fastapi import APIRouter, HTTPException
from models import Alerta
from core.gestor_eventos import procesar_alerta

router = APIRouter()

alertas_db = []

@router.post("/nueva")
def crear_alerta(alerta: Alerta):
    try:
        resultado = procesar_alerta(alerta.model_dump())
        alertas_db.append({
            "alerta": alerta.model_dump(),
            "resultado": resultado
        })
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def listar_alertas():
    return alertas_db

@router.get("/ultimas/{n}")
def ultimas_alertas(n: int = 5):
    return alertas_db[-n:] if alertas_db else []
