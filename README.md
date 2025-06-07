# 🧠 RISK-EYE · AI for Safer Industrial Operations

[//]: # (![BASF]&#40;https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fes%2Ffree-png-tvzsn&psig=AOvVaw2xkjM2GnDbPFYewz-VDR2s&ust=1749405460308000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLCFgKvx340DFQAAAAAdAAAAABAE&#41;)

[//]: # ()

[//]: # (![Microsoft Azure]&#40;https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Microsoft_Azure.svg/320px-Microsoft_Azure.svg.png&#41;)

[//]: # ()

[//]: # (![Ingenio Hackathon]&#40;https://ingenio.org.uy/wp-content/uploads/2020/08/logo.png&#41;)

---

## 🔍 ¿Qué es **RISK-EYE**?

**RISK-EYE** es una API inteligente desarrollada durante la [Hackatón BASF 2025](https://ingenio.org.uy/), que evalúa *
*riesgos cualitativos asociados a tareas industriales** como mantenimiento, inspección, carga/descarga o transferencia
de químicos.

Se basa en:

- 🧠 **Modelos de IA** para detección de pictogramas de riesgo (YOLOv8)
- 📜 **Historial de accidentes y mantenimientos**
- 🤖 **Evaluaciones con OpenAI** (Azure OpenAI)
- 🔗 Infraestructura ligera con **FastAPI + Docker**

---

## 🚀 ¿Cómo levantar el proyecto localmente?

1. **Clonar el repositorio**

```bash
git clone https://github.com/gbaup/hackaton-basf-2025
cd hackaton-basf-2025
````

2. **Crear archivo `.env` en la raíz**

```env
ROBOFLOW_API_KEY=tu_clave_de_roboflow
AZURE_OPENAI_API_KEY=tu_clave_openai
AZURE_OPENAI_ENDPOINT=https://tu-endpoint.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=nombre_del_modelo_deployment
```

3. **Levantar con Docker**

```bash
docker compose up --build -d
```

4. Accedé a la API en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📦 Dependencias principales

* FastAPI
* Uvicorn
* Python 3.11+
* requests
* openai (Azure SDK)

---

## 🤖 Casos de uso

* Predictivo en tareas de alto riesgo
* Detección automática de peligros vía imágenes
* Justificación de niveles de riesgo con historial de incidentes

