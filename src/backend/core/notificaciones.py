import json
import os
from iot.protocolos.mqtt_client import publicar_alerta

TOPIC_ALERTAS = os.getenv("MQTT_TOPIC_ALERTAS", "gia/alertas")
TOPIC_NOTIFICACIONES = os.getenv("MQTT_TOPIC_NOTIFICACIONES", "gia/notificaciones")

def enviar_notificacion(mensaje: dict):
    print("Notificacion recibida:", json.dumps(mensaje, indent=2))
    try:
        publicar_alerta(mensaje)
    except Exception as e:
        print(f"MQTT no disponible ({e}), mensaje solo en consola")
