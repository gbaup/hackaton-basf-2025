from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))
db = client["basf"]
collection = db["historial_mantenimientos"]


def obtener_historial_por_zona(zona: str):
    registros = collection.find({"sector": f"zona_{zona}"})
    historial = []
    for reg in registros:
        pieza = reg.get("id_pieza")
        tarea = reg.get("tipo_tarea")
        resultado = reg.get("resultado")
        obs = reg.get("observaciones", "")
        etiquetas = reg.get("etiquetas_detectadas", [])
        fecha = reg.get("fecha")
        if isinstance(fecha, datetime):
            fecha = fecha.strftime("%Y-%m-%d")
        else:
            fecha = str(fecha)

        resumen = (
            f"📍 Pieza {pieza}, tarea: '{tarea}' en fecha {fecha}.\n"
            f"    - Resultado: {resultado}\n"
            f"    - Observaciones: {obs}"
        )
        historial.append(resumen)

    return historial
