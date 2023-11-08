from fastapi import FastAPI
from routers import demo

app = FastAPI()
app.include_router(demo.router)
