from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .scraper import find_auth_component
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="Authentication Component Detector")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze")
def analyze(url: str):
    result = find_auth_component(url)
    return result


@app.get("/")
def root():
    return {
        "message": "Auth Component Detector is running. Use /analyze?url=..."
    }

