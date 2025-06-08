from pymongo import MongoClient
from datetime import datetime, timedelta
import random
import os

ZONAS = ["zona_A", "zona_B", "zona_C"]
ETIQUETAS = ["inflamable", "corrosivo", "tóxico", "explosivo", "gas a presión"]
OBSERVACIONES = [
    "Oxidación leve detectada en la base de la válvula secundaria.",
    "Se encontraron restos de sustancia corrosiva en el piso.",
    "Etiqueta de advertencia parcialmente desprendida.",
    "Fuga mínima detectada en acople izquierdo, sin riesgo inmediato.",
    "Todo el sistema se encuentra en condiciones óptimas.",
    "Se recomienda limpieza preventiva del conducto principal.",
    "Registro de olor fuerte, posiblemente relacionado a solventes.",
    "Sistema de ventilación funcionando a capacidad reducida.",
    "Trazas de líquido inflamable cerca de la bomba secundaria.",
    "Panel de advertencia visual obstruido por objetos.",
    "Historial de intervención reciente, sin anomalías visibles.",
    "Se observó formación de condensación inusual en la tubería.",
    "Mantenimiento realizado correctamente, sin hallazgos negativos.",
    "Registro de temperatura más alta de lo habitual en la zona.",
    "Zona con acceso restringido por reparación previa aún en curso.",
    "Se detectó un pitido constante en sensor de presión.",
    "Falta de señalización en una de las válvulas críticas.",
    "Se requiere verificar presión del sistema antes de la próxima tarea.",
    "Observación rutinaria sin novedades relevantes.",
    "Historial indica dos incidentes menores en los últimos seis meses."
]
TIPOS_PIEZA = ["VALV", "BOMB", "DUCT", "SENS", "MOTR"]


def generar_mock():
    tipo = random.choice(TIPOS_PIEZA)
    numero = f"{random.randint(1, 9999):04}"
    return {
        "sector": random.choice(ZONAS),
        "id_pieza": f"{tipo}-{numero}",
        "fecha": datetime.now() - timedelta(days=random.randint(1, 365)),
        "etiquetas_detectadas": random.sample(ETIQUETAS, k=random.randint(1, 3)),
        "tipo_tarea": random.choice(
            ["inspección general", "revisión de válvulas", "limpieza", "reemplazo de componentes"]),
        "resultado": random.choice(["sin incidentes", "riesgo leve", "riesgo alto"]),
        "observaciones": random.choice(OBSERVACIONES)
    }


def seed():
    print("🔄 Iniciando migración/Seeder de historial de mantenimientos...")
    client = MongoClient(os.getenv("MONGO_URL"))
    db = client["basf"]
    collection = db["historial_mantenimientos"]

    collection.delete_many({})

    registros = [generar_mock() for _ in range(100)]
    collection.insert_many(registros)
    print("✅ Migración/Seeder completado.")


if __name__ == "__main__":
    seed()
