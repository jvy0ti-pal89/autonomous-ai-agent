from fastapi import FastAPI

from dotenv import load_dotenv
import os

load_dotenv()


from app.api.routes import router

app = FastAPI(title="Autonomous AI Agent")
app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Autonomous AI Agent is running"}
