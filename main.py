from fastapi import FastAPI
from routes import auth, symptoms

app = FastAPI()

app.include_router(auth.router)
app.include_router(symptoms.router)