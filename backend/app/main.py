from fastapi import FastAPI, File, UploadFile, Form

from pydantic import BaseModel
from app.services.risk_service import risk_evaluation
from app.rag_system.rag_engine import generate_response

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "RISK-EYE API is running 🚀"}


@app.post("/predict-risks")
async def predict(file: UploadFile = File(...), zona: str = Form(...)):
    contents = await file.read()
    print("❗️ Imagen recibida", flush=True)
    try:
        return risk_evaluation(contents, file.content_type, zona)
    except Exception:
        return {"error": "Failed to process the image."}


# NUEVO ENDPOINT RAG
class GHSQuery(BaseModel):
    question: str


@app.post("/consulta-ghs")
def consulta_ghs(query: GHSQuery):
    return {"respuesta": generate_response(query.question)}
