from fastapi import FastAPI
from app.routes import router

app = FastAPI(title='Test Restaurant API')
app.include_router(router)
