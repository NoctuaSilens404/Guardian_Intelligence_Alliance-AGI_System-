import json
import os
import logging

logger = logging.getLogger(__name__)

BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC_ALERTAS = os.getenv("MQTT_TOPIC_ALERTAS", "gia/alertas")
TOPIC_NOTIFICACIONES = os.getenv("MQTT_TOPIC_NOTIFICACIONES", "gia/notificaciones")
USERNAME = os.getenv("MQTT_USERNAME", "")
PASSWORD = os.getenv("MQTT_PASSWORD", "")

def publicar_alerta(data: dict):
    try:
        import paho.mqtt.client as mqtt
        client = mqtt.Client()
        if USERNAME and PASSWORD:
            client.username_pw_set(USERNAME, PASSWORD)
        client.connect(BROKER, PORT, 60)
        payload = json.dumps(data)
        client.publish(TOPIC_ALERTAS, payload)
        client.disconnect()
        logger.info("Alerta publicada en MQTT: %s", TOPIC_ALERTAS)
    except ImportError:
        logger.warning("paho-mqtt no instalado, alerta solo en consola")
    except Exception as e:
        logger.error("Error MQTT: %s", e)

def iniciar_cliente():
    import paho.mqtt.client as mqtt

    def on_connect(client, userdata, flags, rc):
        logger.info("Conectado al broker MQTT codigo: %s", rc)
        client.subscribe(TOPIC_NOTIFICACIONES)

    def on_message(client, userdata, msg):
        logger.info("Mensaje recibido [%s]: %s", msg.topic, msg.payload.decode())

    client = mqtt.Client()
    if USERNAME and PASSWORD:
        client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_forever()
