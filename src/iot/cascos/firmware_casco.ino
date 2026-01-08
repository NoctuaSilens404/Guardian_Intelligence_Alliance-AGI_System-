#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "TU_WIFI";
const char* password = "TU_PASSWORD";

const char* mqtt_server = "test.mosquitto.org";
WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("CascoInteligente")) {
      client.subscribe("agi-system/alertas");
    } else {
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Simulación de alerta
  String payload = "{\"trabajador_id\":1, \"tipo\":\"caida\"}";
  client.publish("agi-system/alertas", payload.c_str());
  delay(5000);
}
