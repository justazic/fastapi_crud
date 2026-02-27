from fastapi import FastAPI
from database import engine
import models
from product_router import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)