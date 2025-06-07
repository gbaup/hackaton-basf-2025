import os
from fastapi import APIRouter, File, UploadFile
import requests

router = APIRouter()

API_KEY = os.getenv("ROBOFLOW_API_KEY")
MODEL_ENDPOINT = os.getenv("ROBOFLOW_MODEL_ENDPOINT")


@router.post("/test-roboflow")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        response = requests.post(
            f"{MODEL_ENDPOINT}?api_key={API_KEY}",
            files={"file": ("filename", contents, file.content_type)}
        )
        return response.json()
    except requests.RequestException as e:
        return {"error": "Failed to process the image."}
