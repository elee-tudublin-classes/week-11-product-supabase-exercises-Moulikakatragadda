from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from starlette.config import Config

router = APIRouter()
config = Config(".env")
templates = Jinja2Templates(directory="app/view_templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    serverTime = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    return templates.TemplateResponse("home/index.html", {"request": request, "serverTime": serverTime})

@router.get("/advice", response_class=HTMLResponse)
async def advice(request: Request):
    requests_client = request.app.requests_client
    response = await requests_client.get(config("ADVICE_URL"))
    data = response.json()
    return templates.TemplateResponse("home/advice.html", {"request": request, "data": data})
