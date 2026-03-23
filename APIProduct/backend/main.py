from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from routers import products

app = FastAPI(title="HW Shop")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api")

frontend = os.path.join(os.path.dirname(__file__), "..", "frontend")

@app.get("/")
async def root():
    return FileResponse(os.path.join(frontend, "index.html"))

app.mount("/static", StaticFiles(directory=frontend), name="static")