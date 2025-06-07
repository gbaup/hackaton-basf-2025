from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "RISK-EYE API is running 🚀"}
