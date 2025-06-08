from app.rag_system.pdf_parser import extract_chunks_from_pdf
from app.rag_system.rag_engine import build_faiss_index

if __name__ == "__main__":
    try:
        print("🔍 Extrayendo chunks del PDF...", flush=True)
        chunks = extract_chunks_from_pdf("app/rag_system/ghs_documents/ghs.pdf")
        print(f"✅ Se extrajeron {len(chunks)} chunks.", flush=True)

        print("🧠 Generando embeddings y construyendo índice FAISS...", flush=True)
        build_faiss_index(chunks)

    except Exception as e:
        print("❌ Error al construir el índice:", str(e))
