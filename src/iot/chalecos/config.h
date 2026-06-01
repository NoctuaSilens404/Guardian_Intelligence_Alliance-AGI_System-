// config.h - Configuracion centralizada para firmware GIA

#ifndef CONFIG_H
#define CONFIG_H

#define WIFI_SSID "TU_WIFI"
#define WIFI_PASSWORD "TU_PASSWORD"

#define MQTT_BROKER "localhost"
#define MQTT_PORT 1883
#define MQTT_USER ""
#define MQTT_PASS ""

#define TOPIC_ALERTAS "gia/alertas"
#define TOPIC_COMANDOS "gia/comandos"
#define TRABAJADOR_ID 2

#define PIN_PULSO 34
#define PIN_TEMP 35
#define PIN_SPO2 32
#define PIN_BOTON_PANICO 25

#endif
