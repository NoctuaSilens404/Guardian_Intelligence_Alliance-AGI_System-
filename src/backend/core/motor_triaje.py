def clasificar_evento(data: dict) -> str:
    """
    Clasifica la gravedad de un evento basado en signos vitales y tipo de alerta.
    """

    tipo = data.get("tipo")
    signos = data.get("signos_vitales", {})

    # Reglas simples iniciales (luego se reemplazarán con IA real)
    if tipo == "caida":
        return "alta"

    if signos.get("pulso", 0) < 40 or signos.get("pulso", 0) > 160:
        return "critica"

    if signos.get("temperatura", 0) > 39:
        return "alta"

    return "normal"
