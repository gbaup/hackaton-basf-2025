import os
import requests

API_KEY = os.getenv("ROBOFLOW_API_KEY")
MODEL_ENDPOINT = os.getenv("ROBOFLOW_MODEL_ENDPOINT")


def ghs_labels_detection(contents: bytes, content_type: str):
    print("🔍 Iniciando detección de etiquetas SGA...", flush=True)
    response = requests.post(
        f"{MODEL_ENDPOINT}?api_key={API_KEY}",
        files={"file": ("filename", contents, content_type)}
    )
    result = response.json()
    detected_classes = [pred["class"] for pred in result.get("predictions", [])]
    return list(set(detected_classes))
