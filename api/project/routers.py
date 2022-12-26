from fastapi import FastAPI
from dotenv import load_dotenv
from project.infrastructure.open_api.open_api_schema import Schema
from project.resources.lifecheck.controller import router as life_check_api

app = FastAPI()
load_dotenv()

# app routes
app.include_router(life_check_api, prefix="/health", tags=["health"])

schema = Schema(app=app, title="Microservices template")
app.openapi = schema.create
