#include <WiFi.h>
#include <PubSubClient.h>
#include "config.h"

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.print("Conectando a ");
  Serial.println(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" WiFi conectado");
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Conectando MQTT...");
    if (client.connect("CascoInteligente", MQTT_USER, MQTT_PASS)) {
      Serial.println("conectado");
      client.subscribe(TOPIC_COMANDOS);
    } else {
      Serial.print("fallo, rc=");
      Serial.print(client.state());
      delay(5000);
    }
  }
}

void leer_sensores() {
  int pulso = analogRead(PIN_PULSO);
  float temperatura = (analogRead(PIN_TEMP) * 3.3 / 4095.0) * 100.0;
  int spo2 = map(analogRead(PIN_SPO2), 0, 4095, 85, 100);
  int caida = digitalRead(PIN_CAIDA);

  String payload = "{";
  payload += "\"trabajador_id\":";
  payload += TRABAJADOR_ID;
  payload += ",\"tipo\":\"";
  payload += (caida == HIGH) ? "caida" : "signos";
  payload += "\",\"signos_vitales\":{";
  payload += "\"pulso\":" + String(pulso) + ",";
  payload += "\"temperatura\":" + String(temperatura) + ",";
  payload += "\"spo2\":" + String(spo2);
  payload += "}}";

  client.publish(TOPIC_ALERTAS, payload.c_str());
}

void setup() {
  Serial.begin(115200);
  pinMode(PIN_PULSO, INPUT);
  pinMode(PIN_TEMP, INPUT);
  pinMode(PIN_SPO2, INPUT);
  pinMode(PIN_CAIDA, INPUT_PULLUP);
  pinMode(PIN_BOTON_PANICO, INPUT_PULLUP);

  setup_wifi();
  client.setServer(MQTT_BROKER, MQTT_PORT);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  if (digitalRead(PIN_BOTON_PANICO) == LOW) {
    String payload = "{\"trabajador_id\":";
    payload += TRABAJADOR_ID;
    payload += ",\"tipo\":\"panico\"}";
    client.publish(TOPIC_ALERTAS, payload.c_str());
    delay(10000);
  }

  leer_sensores();
  delay(5000);
}
