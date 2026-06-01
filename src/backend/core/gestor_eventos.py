from core.motor_triaje import clasificar_evento
from core.notificaciones import enviar_notificacion

def procesar_alerta(data: dict) -> dict:
    nivel = clasificar_evento(data)

    mensaje = {
        "trabajador_id": data.get("trabajador_id"),
        "tipo_alerta": data.get("tipo"),
        "nivel_gravedad": nivel,
        "signos_vitales": data.get("signos_vitales", {}),
        "ubicacion": data.get("ubicacion", {})
    }

    enviar_notificacion(mensaje)

    return {
        "status": "procesado",
        "nivel_gravedad": nivel
    }
