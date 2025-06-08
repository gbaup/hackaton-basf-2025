import os
import json
from openai import AzureOpenAI
from fastapi import HTTPException
from app.models.evaluation import EvaluationResponse

from app.rag_system.rag_engine import query_index

client = AzureOpenAI(
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


def evaluar_riesgo(mensaje: str) -> EvaluationResponse:
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Sos un experto en seguridad industrial y prevención de riesgos químicos. "
                        "Tu respuesta debe estar en formato JSON con las claves: "
                        "'riesgo_estimado', 'motivos' (lista), y 'sugerencias' (lista). "
                        "'riesgo_estimado' debe ser uno de: alto, medio o bajo, basándote en la norma GHS. "
                        "Si el mensaje recibido es de otros temas, respondé en texto plano por qué no podés ayudar con eso."
                    )
                },
                {
                    "role": "user",
                    "content": mensaje,
                }
            ],
            model=deployment,
            max_tokens=800,
            temperature=0.9,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        response_text = response.choices[0].message.content

        try:
            data = json.loads(response_text)
            return EvaluationResponse(**data)
        except json.JSONDecodeError:
            raise HTTPException(
                status_code=422,
                detail={"error": "Pregunta no válida", "mensaje": response_text}
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": str(e)})
