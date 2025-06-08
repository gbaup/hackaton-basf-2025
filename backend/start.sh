#!/bin/bash
set -e

echo "🏗️  Verificando existencia de índice FAISS..."

if [ ! -f app/rag_system/faiss_index/index.faiss ]; then
  echo "📚 No se encontró índice. Ejecutando build_index.py..."
  python -m app.rag_system.build_index
else
  echo "✅ Índice ya existente. No se vuelve a construir."
fi

echo "🚀 Lanzando API FastAPI..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
