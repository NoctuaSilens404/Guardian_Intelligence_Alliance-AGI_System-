# GIA - Guardian Intelligence Alliance
# Arquitectura General del Sistema

## Visión General

Sistema de monitoreo preventivo y respuesta a emergencias para
trabajadores industriales en entornos de alto riesgo. El EPP
tradicional se convierte en una red activa de sensores que
colabora con una IA para prevenir accidentes en tiempo real.

## Componentes Principales

### 1. Guardian Shell (Hardware)
Dispositivos IoT basados en ESP32:
- **Casco inteligente**: sensores biométricos + detección de caídas
- **Chaleco inteligente**: sensores biométricos
- Comunicación vía MQTT
- Alerta visual (RGB), sonora (buzzer) y botón de pánico

### 2. Alliance Core (Backend)
API REST en FastAPI:
- `POST /api/v1/alertas/nueva` - recepción de alertas IoT
- `GET /api/v1/alertas/` - listar alertas
- `GET /api/v1/alertas/ultimas/{n}` - últimas n alertas
- `POST /api/v1/trabajadores/` - registrar trabajador
- `GET /api/v1/trabajadores/` - listar trabajadores
- `PUT /api/v1/trabajadores/{id}/desactivar` - desactivar

### 3. Motor de IA (Machine Learning)
Clasificador RandomForest para riesgo de fatiga:
- Features: pulso, temperatura, SpO2, horas trabajadas
- Etiquetas: bajo, medio, alto
- Pipeline: StandardScaler + RandomForestClassifier
- Almacenado con joblib para inferencia rápida

### 4. Seguridad (Digital Shield)
- Cifrado extremo a extremo
- Protocolo "break-glass" para emergencias
- Historial anonimizado

## Flujo de Datos

```
ESP32 (Casco/Chaleco)
    │
    ▼  MQTT
Broker Mosquitto
    │
    ▼
Backend FastAPI
    │
    ├─▶ Motor de Triaje (clasificación)
    │       │
    │       ▼
    │   Predictor IA (riesgo de fatiga)
    │
    └─▶ Notificaciones
            │
            ├─▶ Dashboard (WebSocket)
            └─▶ MQTT (comandos a dispositivos)
```

### 5. Dashboard (Monitoreo en Tiempo Real)
Interfaz web para supervisión:
- **URL**: `/dashboard`
- **WebSocket**: `/dashboard/ws` para alertas en vivo
- **Métricas**: trabajadores activos, total alertas, alertas críticas
- **Feed**: historial de alertas en tiempo real

## Stack Tecnológico

- Backend: Python 3.14+, FastAPI, Uvicorn
- Dashboard: HTML, CSS, JavaScript vanilla, WebSockets
- IA: scikit-learn, pandas, joblib
- IoT: C++ (Arduino/ESP32), MQTT, PubSubClient
- Testing: pytest, httpx
