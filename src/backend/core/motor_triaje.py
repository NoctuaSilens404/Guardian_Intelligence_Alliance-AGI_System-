from ia.inferencia.predictor_riesgo import predecir_riesgo_fatiga

def clasificar_evento(data: dict) -> str:
    tipo = data.get("tipo")
    signos = data.get("signos_vitales", {})

    if tipo == "caida":
        return "alta"
    if tipo == "panico":
        return "critica"

    if signos:
        resultado_ia = predecir_riesgo_fatiga(signos)
        riesgo = resultado_ia.get("riesgo")

        if riesgo == "alto":
            return "critica"
        if riesgo == "medio":
            return "alta"
        if riesgo == "bajo":
            return "normal"

    return "normal"
