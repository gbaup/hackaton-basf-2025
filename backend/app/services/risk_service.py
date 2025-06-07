from app.services.roboflow_service import ghs_labels_detection
from app.services.openai_service import evaluar_riesgo


def risk_evaluation(contents: bytes, content_type: str):
    detected_classes = ghs_labels_detection(contents, content_type)

    responses = {}
    for detected_class in detected_classes:
        mensaje = f"Detecté el pictograma: {detected_class}. ¿Cuál es el riesgo asociado?"
        response = evaluar_riesgo(mensaje)
        responses[detected_class] = response

    return {"resultados": responses}
