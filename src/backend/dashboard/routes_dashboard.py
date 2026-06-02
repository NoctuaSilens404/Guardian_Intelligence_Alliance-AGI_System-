from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import os

router = APIRouter()

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")

def _read_html(name: str) -> str:
    path = os.path.join(TEMPLATES_DIR, name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

LOGIN_HTML = _read_html("login.html")
DASHBOARD_HTML = _read_html("dashboard.html")

@router.get("/login", response_class=HTMLResponse)
async def login_page():
    return LOGIN_HTML

@router.post("/login")
async def login(password: str = Form(...)):
    from app import DASHBOARD_PASS
    if password == DASHBOARD_PASS:
        resp = RedirectResponse(url="/dashboard/", status_code=302)
        resp.set_cookie(key="gia_session", value=password, httponly=True, max_age=86400)
        return resp
    html = LOGIN_HTML.replace("{% if error %}<div class=\"error\">{{ error }}</div>{% endif %}", '<div class="error">Contraseña incorrecta</div>')
    return HTMLResponse(html)

@router.get("/logout")
async def logout():
    resp = RedirectResponse(url="/dashboard/login")
    resp.delete_cookie("gia_session")
    return resp

@router.get("/", response_class=HTMLResponse)
async def dashboard():
    return DASHBOARD_HTML
