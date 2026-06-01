from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from api.routes_alertas import router as alertas_router
from api.routes_trabajadores import router as trabajadores_router
from dashboard.routes_dashboard import router as dashboard_router
from models import Trabajador, Alerta
from api.routes_alertas import crear_alerta
from api.routes_trabajadores import crear_trabajador
import os

app = FastAPI(
    title="Guardian Intelligence Alliance - API",
    description="Backend del sistema de monitoreo preventivo GIA",
    version="0.1.0"
)

DASHBOARD_PASS = os.getenv("GIA_PASSWORD", "admin123")

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if request.url.path.startswith("/dashboard") and request.url.path != "/dashboard/login":
        auth = request.headers.get("x-gia-key", "")
        cookie = request.cookies.get("gia_session", "")
        if auth != DASHBOARD_PASS and cookie != DASHBOARD_PASS:
            if request.url.path == "/dashboard/" or request.url.path.startswith("/dashboard?") or request.url.path == "/dashboard":
                from fastapi.responses import RedirectResponse
                return RedirectResponse(url="/dashboard/login")
            return JSONResponse(status_code=401, content={"detail": "No autorizado"})
    return await call_next(request)

app.include_router(alertas_router, prefix="/api/v1/alertas", tags=["Alertas"])
app.include_router(trabajadores_router, prefix="/api/v1/trabajadores", tags=["Trabajadores"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])

@app.get("/health")
def health_check():
    return {"status": "ok", "sistema": "GIA - Guardian Intelligence Alliance"}

@app.on_event("startup")
async def seed_data():
    if not trabajadores_router.trabajadores_db:
        for w in [
            Trabajador(id=1, nombre="Carlos", apellido="Mendoza", dni="12345678", rol="Soldador"),
            Trabajador(id=2, nombre="Ana", apellido="López", dni="23456789", rol="Supervisora"),
            Trabajador(id=3, nombre="Pedro", apellido="Ramírez", dni="34567890", rol="Electricista"),
            Trabajador(id=4, nombre="María", apellido="García", dni="45678901", rol="Operaria"),
        ]:
            crear_trabajador(w)

    if not alertas_router.alertas_db:
        for a in [
            Alerta(trabajador_id=1, tipo="signos", signos_vitales={"pulso": 78, "temperatura": 36.8, "spo2": 97, "horas_trabajadas": 4}),
            Alerta(trabajador_id=2, tipo="signos", signos_vitales={"pulso": 95, "temperatura": 37.5, "spo2": 95, "horas_trabajadas": 6}),
            Alerta(trabajador_id=3, tipo="signos", signos_vitales={"pulso": 120, "temperatura": 37.8, "spo2": 92, "horas_trabajadas": 8}),
            Alerta(trabajador_id=4, tipo="signos", signos_vitales={"pulso": 60, "temperatura": 36.5, "spo2": 98, "horas_trabajadas": 3}),
            Alerta(trabajador_id=1, tipo="caida"),
            Alerta(trabajador_id=3, tipo="signos", signos_vitales={"pulso": 142, "temperatura": 38.9, "spo2": 89, "horas_trabajadas": 10}),
            Alerta(trabajador_id=2, tipo="panico"),
        ]:
            crear_alerta(a)
