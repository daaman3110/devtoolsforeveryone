from fastapi import FastAPI
from api.json_tools import router as json_router

app = FastAPI(
    title="DevTools for everyone",
    description="Simple, fast and beginner-friendly developer utilities",
    version="1.0.0",
)

# Include JSON router
app.include_router(json_router)
