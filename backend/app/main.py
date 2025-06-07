from fastapi import FastAPI, File, UploadFile

from app.services.risk_service import risk_evaluation

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "RISK-EYE API is running 🚀"}


@app.post("/predict-risks")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        return risk_evaluation(contents, file.content_type)
    except Exception:
        return {"error": "Failed to process the image."}
