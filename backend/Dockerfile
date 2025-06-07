FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "-c", "python app/migrations/seed_historial_mantenimientos.py && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
