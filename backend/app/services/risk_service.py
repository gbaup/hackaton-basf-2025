from app.services.roboflow_service import ghs_labels_detection
from app.services.history_service import obtener_historial_por_zona
from app.services.openai_service import evaluar_riesgo

from app.rag_system.rag_engine import query_index


def risk_evaluation(contents: bytes, content_type: str, zona: str):
    detected_classes = ghs_labels_detection(contents, content_type)
    print(f"⚠️  Clases detectadas: {detected_classes}", flush=True)
    historial_context = obtener_historial_por_zona(zona)
    responses = {}
    print("🧠 Evaluando riesgo contextualizado con OpenAI...", flush=True)
    for detected_class in detected_classes:
        ghs_chunks = query_index(detected_class)

        mensaje = (
                f"Detecté el pictograma: '{detected_class}'.\n\n"
                "📘 Según la normativa GHS:\n"
                + "\n\n".join(ghs_chunks[:3]) +
                "\n\n📂 Historial de tareas previas en la zona:\n" +
                "\n\n".join(historial_context[:5]) +  # limitar para evitar tokens
                "\n\n🧠 Con base en esta información, indicá el riesgo estimado, los motivos y sugerencias."
        )

        response = evaluar_riesgo(mensaje)
        responses[detected_class] = response

    print(f"✅ Evaluación de riesgos completada!")
    return {"zona": zona, "resultados": responses}
