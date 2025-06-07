import os
import requests

API_KEY = os.getenv("ROBOFLOW_API_KEY")
MODEL_ENDPOINT = os.getenv("ROBOFLOW_MODEL_ENDPOINT")


def predict_image(contents: bytes, content_type: str):
    response = requests.post(
        f"{MODEL_ENDPOINT}?api_key={API_KEY}",
        files={"file": ("filename", contents, content_type)}
    )
    return response.json()
