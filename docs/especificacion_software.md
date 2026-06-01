# GIA - Guardian Intelligence Alliance

## Especificación del Software

### Backend (FastAPI)
- Python 3.14+
- FastAPI con Uvicorn
- Endpoints REST documentados con OpenAPI
- Formato de intercambio: JSON

### Modelo de IA
- Algoritmo: RandomForestClassifier
- Preprocesamiento: StandardScaler
- Features: pulso, temperatura, SpO2, horas_trabajadas
- Salida: riesgo (bajo/medio/alto)

### Comunicación IoT
- Protocolo: MQTT v3.1.1
- Broker: Mosquitto
- Topics:
  - `gia/alertas` - datos de sensores y alertas
  - `gia/comandos` - comandos a dispositivos
  - `gia/notificaciones` - notificaciones del backend
