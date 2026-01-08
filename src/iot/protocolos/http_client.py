import requests

BACKEND_URL = "http://localhost:8000/alertas/nueva"

def enviar_alerta_http(data: dict):
    try:
        response = requests.post(BACKEND_URL, json=data)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
