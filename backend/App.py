from fastapi import FastAPI
from routes.hate_predictor import predictor
 
app = FastAPI()
app.include_router(predictor)