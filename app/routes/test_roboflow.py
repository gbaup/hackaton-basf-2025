import os
from fastapi import APIRouter, File, UploadFile
import requests

router = APIRouter()

API_KEY = os.getenv("ROBOFLOW_API_KEY")
MODEL_ENDPOINT = "https://detect.roboflow.com/my-first-project-zzejr-instant-2"


@router.post("/test-roboflow")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    print(f"{MODEL_ENDPOINT}?api_key={API_KEY}")
    try:
        response = requests.post(
            f"{MODEL_ENDPOINT}?api_key={API_KEY}",
            files={"file": ("filename", contents, file.content_type)}
        )
        print(response.status_code, response.text)
        return response.json()
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return {"error": "Failed to process the image."}
