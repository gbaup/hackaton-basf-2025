# 🧠 RISK-EYE · AI for Safer Industrial Operations

[//]: # (![BASF]&#40;https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/BASF-Logo_bw.svg/320px-BASF-Logo_bw.svg.png&#41;)

[//]: # (![Microsoft Azure]&#40;https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Microsoft_Azure.svg/320px-Microsoft_Azure.svg.png&#41;)

[//]: # (![Ingenio Hackathon]&#40;https://ingenio.org.uy/wp-content/uploads/2020/08/logo.png&#41;)

---

## 🧪 Problema

Las tareas de mantenimiento, carga/descarga, inspección o manipulación de sustancias químicas en plantas industriales
como BASF implican **riesgos críticos de exposición por inhalación y de impacto ambiental**.

La falta de herramientas automatizadas para prever estos riesgos puede derivar en:

- Accidentes por manipulación inadecuada
- Emisiones no controladas
- Daños a la salud del personal y al medio ambiente

---

## ✅ Nuestra solución: **RISK-EYE**

**RISK-EYE** es una API inteligente que **evalúa cualitativamente el riesgo** de una tarea industrial **antes de
ejecutarla**, combinando:

- 📷 **Análisis de imágenes**: detección de pictogramas de riesgo (modelo YOLOv8)
- 📊 **Historial de incidentes simulados**: base de datos con accidentes y mantenimientos pasados
- 🧠 **Evaluación IA**: modelo de lenguaje de Azure OpenAI que estima el riesgo, explica las causas y sugiere medidas

---

## 🛠️ Tecnologías aplicadas

| Área                  | Herramienta                    |
|-----------------------|--------------------------------|
| Backend API           | FastAPI (Python)               |
| Containerización      | Docker                         |
| AI (detección visual) | Roboflow + YOLOv8              |
| AI (evaluación texto) | Azure OpenAI (GPT)             |
| Mock de datos         | Base NoSQL embebida (simulada) |

---

## 🚀 ¿Cómo probarlo localmente?

1. **Clonar el repositorio**

```bash
git clone https://github.com/gbaup/hackaton-basf-2025.git
cd hackaton-basf-2025
````

2. **Crear el archivo `.env`**

```env
ROBOFLOW_MODEL_ENDPOINT=tu_endpoint_roboflow
ROBOFLOW_API_KEY=tu_clave_roboflow
AZURE_OPENAI_API_KEY=tu_clave_openai
AZURE_OPENAI_ENDPOINT=https://tu-endpoint.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=nombre_del_modelo
AZURE_OPENAI_API_VERSION=fecha_de_version
MONGO_URL=mongodb://mongo:27017
```

3. **Levantar la API con Docker**

```bash
docker compose up --build -d
```

4. 📎 Accedé a la documentación y probá los endpoints en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 ¿Qué simula?

> Al no tener acceso a datos reales, la solución **incluye una base de datos ficticia** con registros históricos de
> incidentes, mantenimientos y tareas por tipo. Esto permite a la IA contextualizar mejor los riesgos.

---

## 📌 Conclusión

**RISK-EYE** propone una solución **simple, eficaz y extensible** para mitigar riesgos operativos antes de que ocurran.
Su diseño permite integrarse fácilmente con sistemas existentes y escalar a distintos entornos industriales.

---

🧠 *Desarrollado en la Hackatón BASF 2025*


