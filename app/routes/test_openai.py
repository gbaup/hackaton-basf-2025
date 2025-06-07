import os
from fastapi import APIRouter
from pydantic import BaseModel
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()


class ChatRequest(BaseModel):
    mensaje: str


@router.post("/test-openai")
def test_openai_endpoint(request: ChatRequest):
    client = AzureOpenAI(
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_KEY"),
    )

    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Sos un experto en seguridad industrial y prevención de riesgos químicos. Ayudás a evaluar riesgos en tareas de mantenimiento, inspección y manipulación de sustancias peligrosas en una planta. Tu evaluación es extremadamente importante, ya que un accidente no solo representa pérdidas economómicas para la empresa sino que puede también involucrar pérdidas humanas",
            },
            {
                "role": "user",
                "content": request.mensaje,
            }
        ],
        model=deployment,
        max_tokens=800,
        temperature=0.9,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return {
        "respuesta_openai": response.choices[0].message.content
    }
