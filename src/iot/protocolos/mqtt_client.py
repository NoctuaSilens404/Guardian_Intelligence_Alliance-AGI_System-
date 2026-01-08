import paho.mqtt.client as mqtt
import json

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "agi-system/alertas"

def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT con código:", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print("Mensaje recibido:", msg.topic, msg.payload.decode())

def publicar_alerta(data: dict):
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    payload = json.dumps(data)
    client.publish(TOPIC, payload)
    client.disconnect()

def iniciar_cliente():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_forever()
