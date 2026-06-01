import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from backend.core.gestor_eventos import procesar_alerta

def test_procesar_alerta_caida():
    resultado = procesar_alerta({
        "trabajador_id": 1,
        "tipo": "caida",
        "signos_vitales": {}
    })
    assert resultado["status"] == "procesado"
    assert resultado["nivel_gravedad"] == "alta"

def test_procesar_alerta_panico():
    resultado = procesar_alerta({
        "trabajador_id": 2,
        "tipo": "panico",
        "signos_vitales": {}
    })
    assert resultado["status"] == "procesado"
    assert resultado["nivel_gravedad"] == "critica"

def test_procesar_alerta_sin_signos():
    resultado = procesar_alerta({
        "trabajador_id": 3,
        "tipo": "signos",
        "signos_vitales": {}
    })
    assert resultado["status"] == "procesado"
    assert resultado["nivel_gravedad"] == "normal"
