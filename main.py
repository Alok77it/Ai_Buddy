from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from gemini_utils import ask_gemini

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": None})

@app.post("/", response_class=HTMLResponse)
def chat(request: Request, user_input: str = Form(...)):
    response = ask_gemini(user_input)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "user_input": user_input,
        "response": response
    })

