from fastapi import FastAPI, File, UploadFile
from app.routes import test_openai, test_roboflow

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "RISK-EYE API is running 🚀"}


@app.post("/predict-risks")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        return predict_image(contents, file.content_type)
    except Exception:
        return {"error": "Failed to process the image."}


app.include_router(test_openai.router)
app.include_router(test_roboflow.router)
