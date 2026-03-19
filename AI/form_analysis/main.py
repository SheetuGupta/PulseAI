# e:/videoAI/form_analysis/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.form import router as form_router
import os

app = FastAPI(
    title="PulseAI Form Analysis Module",
    description="Analyzes exercise form from video using MediaPipe and Gemini Vision",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(form_router)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "module": "form_analysis",
        "model": "gemini-2.5-flash",
        "mediapipe": "active"
    }

@app.get("/")
def root():
    return {
        "module": "PulseAI Form Analysis",
        "endpoint": "POST /api/form/analyze",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8001))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
