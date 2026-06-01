from fastapi import APIRouter, HTTPException, Depends, Header
from models import Alerta
from core.gestor_eventos import procesar_alerta
from datetime import datetime
from typing import Optional

router = APIRouter()

alertas_db = []
historial_signos = {}

@router.post("/nueva")
def crear_alerta(alerta: Alerta):
    try:
        resultado = procesar_alerta(alerta.model_dump())
        entry = {
            "alerta": alerta.model_dump(),
            "resultado": resultado,
            "timestamp": datetime.now().isoformat()
        }
        alertas_db.append(entry)

        wid = alerta.trabajador_id
        if wid not in historial_signos:
            historial_signos[wid] = []
        if alerta.signos_vitales:
            historial_signos[wid].append({
                "timestamp": datetime.now().isoformat(),
                "signos": alerta.signos_vitales.model_dump(),
                "nivel": resultado["nivel_gravedad"]
            })
            if len(historial_signos[wid]) > 200:
                historial_signos[wid] = historial_signos[wid][-200:]

        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def listar_alertas():
    return alertas_db

@router.get("/ultimas/{n}")
def ultimas_alertas(n: int = 5):
    return alertas_db[-n:] if alertas_db else []

@router.get("/historial/{trabajador_id}")
def historial_trabajador(trabajador_id: int):
    return historial_signos.get(trabajador_id, [])
