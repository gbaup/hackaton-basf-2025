from pydantic import BaseModel
from typing import List, Optional


class EvaluationRequest(BaseModel):
    ubicacion: str
    pictogramas_detectados: List[str]


class EvaluationResponse(BaseModel):
    riesgo_estimado: str
    motivos: List[str]
    sugerencias: Optional[List[str]] = None
