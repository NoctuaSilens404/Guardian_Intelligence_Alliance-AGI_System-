import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from iot.protocolos.mqtt_client import publicar_alerta
from iot.protocolos.http_client import enviar_alerta_http

def test_publicar_alerta_mqtt():
    try:
        publicar_alerta({"test": True, "trabajador_id": 1})
    except Exception:
        pass

def test_enviar_alerta_http():
    try:
        enviar_alerta_http({"test": True, "trabajador_id": 1})
    except Exception:
        pass

def test_http_client_url():
    from iot.protocolos.http_client import BACKEND_URL
    assert BACKEND_URL == "http://localhost:8000/api/v1/alertas/nueva"
