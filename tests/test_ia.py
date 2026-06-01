import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from ia.inferencia.predictor_riesgo import predecir_riesgo_fatiga

def test_predecir_riesgo_bajo():
    resultado = predecir_riesgo_fatiga({
        "pulso": 70,
        "temperatura": 36.5,
        "spo2": 98,
        "horas_trabajadas": 4
    })
    assert "riesgo" in resultado
    assert "confianza" in resultado
    assert resultado["riesgo"] in ("bajo", "medio", "alto")

def test_predecir_riesgo_alto():
    resultado = predecir_riesgo_fatiga({
        "pulso": 140,
        "temperatura": 39.0,
        "spo2": 88,
        "horas_trabajadas": 10
    })
    assert resultado["riesgo"] in ("bajo", "medio", "alto")

def test_predecir_riesgo_valores_default():
    resultado = predecir_riesgo_fatiga({})
    assert "riesgo" in resultado
