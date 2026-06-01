// config.h - Configuracion centralizada para firmware GIA
// Renombra este archivo a config.h y completa tus credenciales

#ifndef CONFIG_H
#define CONFIG_H

// WiFi
#define WIFI_SSID "TU_WIFI"
#define WIFI_PASSWORD "TU_PASSWORD"

// MQTT
#define MQTT_BROKER "localhost"
#define MQTT_PORT 1883
#define MQTT_USER ""
#define MQTT_PASS ""

// Topics
#define TOPIC_ALERTAS "gia/alertas"
#define TOPIC_COMANDOS "gia/comandos"

// Identificador del dispositivo
#define TRABAJADOR_ID 1

// Pines de sensores (ESP32)
#define PIN_PULSO 34
#define PIN_TEMP 35
#define PIN_SPO2 32
#define PIN_CAIDA 33
#define PIN_BOTON_PANICO 25
#define PIN_LED_ROJO 26
#define PIN_LED_VERDE 27
#define PIN_LED_AZUL 14
#define PIN_BUZZER 12

#endif
