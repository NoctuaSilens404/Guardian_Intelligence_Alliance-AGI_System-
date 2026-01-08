def enviar_notificacion(mensaje: dict):
    """
    Envía una notificación al dashboard o sistema de monitoreo.
    Por ahora solo imprime, luego se conectará a WebSockets o MQTT.
    """
    print("🔔 Notificación enviada:", mensaje)
