from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SignosVitales(BaseModel):
    pulso: int = 80
    temperatura: float = 36.5
    spo2: int = 97
    horas_trabajadas: int = 4

class Alerta(BaseModel):
    trabajador_id: int
    tipo: str
    signos_vitales: Optional[SignosVitales] = None
    ubicacion: Optional[dict] = None

class Trabajador(BaseModel):
    id: int
    nombre: str
    apellido: str
    dni: str
    rol: str
    activo: bool = True

class AlertaDB(BaseModel):
    alerta: dict
    resultado: dict
    timestamp: str = ""
