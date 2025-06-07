from fastapi import FastAPI
from app.routes import test_openai, test_roboflow

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "RISK-EYE API is running 🚀"}


app.include_router(test_openai.router)
app.include_router(test_roboflow.router)
