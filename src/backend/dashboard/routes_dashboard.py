from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os

from dashboard.websocket_manager import manager

router = APIRouter()

templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(request: Request, password: str = Form(...)):
    from app import DASHBOARD_PASS
    if password == DASHBOARD_PASS:
        resp = RedirectResponse(url="/dashboard/", status_code=302)
        resp.set_cookie(key="gia_session", value=password, httponly=True, max_age=86400)
        return resp
    return templates.TemplateResponse("login.html", {"request": request, "error": "Contraseña incorrecta"})

@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@router.get("/logout")
async def logout():
    resp = RedirectResponse(url="/dashboard/login")
    resp.delete_cookie("gia_session")
    return resp

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
