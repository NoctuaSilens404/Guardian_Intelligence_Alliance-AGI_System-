import joblib
import numpy as np
import os
from typing import Dict, Any

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "modelos")
MODEL_PATH = os.path.join(MODEL_DIR, "modelo_riesgo_fatiga.pkl")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")

_model = None
_scaler = None

def _cargar_modelo():
    global _model, _scaler
    if _model is None:
        _model = joblib.load(MODEL_PATH)
        _scaler = joblib.load(SCALER_PATH)

def predecir_riesgo_fatiga(signos_vitales: Dict[str, Any]) -> Dict[str, Any]:
    _cargar_modelo()

    pulso = signos_vitales.get("pulso", 80)
    temperatura = signos_vitales.get("temperatura", 36.5)
    spo2 = signos_vitales.get("spo2", 97)
    horas_trabajadas = signos_vitales.get("horas_trabajadas", 4)

    X = np.array([[pulso, temperatura, spo2, horas_trabajadas]])
    X_scaled = _scaler.transform(X)

    riesgo = _model.predict(X_scaled)[0]
    probabilidades = _model.predict_proba(X_scaled)[0]
    confianza = max(probabilidades)

    niveles_prioridad = {"bajo": 1, "medio": 2, "alto": 3}

    return {
        "riesgo": riesgo,
        "confianza": round(float(confianza), 3),
        "prioridad": niveles_prioridad.get(riesgo, 1),
        "signos_procesados": {
            "pulso": pulso,
            "temperatura": temperatura,
            "spo2": spo2,
            "horas_trabajadas": horas_trabajadas
        }
    }
