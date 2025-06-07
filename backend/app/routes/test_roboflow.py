import os
from fastapi import APIRouter, File, UploadFile
import requests
from app.routes.test_openai import test_openai_endpoint, ChatRequest

router = APIRouter()

API_KEY = os.getenv("ROBOFLOW_API_KEY")
MODEL_ENDPOINT = "https://detect.roboflow.com/my-first-project-zzejr/5"


@router.post("/test-roboflow")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        response = requests.post(
            f"{MODEL_ENDPOINT}?api_key={API_KEY}",
            files={"file": ("filename", contents, file.content_type)}
        )
        result = response.json()
        clases_detectadas = [pred["class"] for pred in result.get("predictions", [])]
        clases_unicas = list(set(clases_detectadas))

        respuestas = {}
        for clase in clases_unicas:
            mensaje = f"Detecté el pictograma: {clase}. ¿Cuál es el riesgo asociado?"
            chat_request = ChatRequest(mensaje=mensaje)
            respuesta = test_openai_endpoint(chat_request)
            respuestas[clase] = respuesta

        return {"resultados": respuestas}

    except requests.RequestException as e:
        return {"error": "Failed to process the image."}
