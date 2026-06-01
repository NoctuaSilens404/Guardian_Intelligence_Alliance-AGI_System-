from fastapi import FastAPI
from api.routes_alertas import router as alertas_router
from api.routes_trabajadores import router as trabajadores_router
from dashboard.routes_dashboard import router as dashboard_router

app = FastAPI(
    title="Guardian Intelligence Alliance - API",
    description="Backend del sistema de monitoreo preventivo GIA",
    version="0.1.0"
)

app.include_router(alertas_router, prefix="/api/v1/alertas", tags=["Alertas"])
app.include_router(trabajadores_router, prefix="/api/v1/trabajadores", tags=["Trabajadores"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])

@app.get("/health")
def health_check():
    return {"status": "ok", "sistema": "GIA - Guardian Intelligence Alliance"}
