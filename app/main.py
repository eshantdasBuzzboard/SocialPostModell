import sys
import os
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import logging

from app.routers import home

# Mount templates with absolute path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

template_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "app", "templates"
)
templates = Jinja2Templates(directory=template_path)


# Include routers
app.include_router(home.router)
# app.include_router(api.router, prefix="/api")
