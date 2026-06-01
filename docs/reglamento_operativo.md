# GIA - Guardian Intelligence Alliance

## Reglamento Operativo

### Niveles de Alerta

| Gravedad | Color | Acción |
|----------|-------|--------|
| Normal | Verde | Monitoreo pasivo |
| Alta | Amarillo | Notificar supervisor |
| Crítica | Rojo | Activar protocolo de emergencia |

### Protocolo de Emergencia
1. Dispositivo detecta anomalía (caída, signos críticos, pánico)
2. Alerta enviada vía MQTT al backend
3. Backend clasifica gravedad con IA
4. Si es crítica: notificación inmediata a brigada de emergencia
5. Break-glass: datos médicos del trabajador liberados para emergencia
