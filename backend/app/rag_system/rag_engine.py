import os
import faiss
import time
import numpy as np
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

embedding_client = AzureOpenAI(
    api_key=os.getenv("AZURE_EMBEDDINGS_KEY"),
    api_version=os.getenv("AZURE_EMBEDDINGS_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_EMBEDDINGS_ENDPOINT")
)

chat_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

INDEX_FILE = "app/rag_system/faiss_index/index.faiss"
CHUNKS_FILE = "app/rag_system/faiss_index/chunks.npy"


def embed(text):
    try:
        response = embedding_client.embeddings.create(
            input=[text],
            model=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT_NAME")
        )
        return np.array(response.data[0].embedding, dtype=np.float32)
    except Exception as e:
        print("❌ Error al generar embedding:", str(e))
        raise


def build_faiss_index(chunks):
    dim = 1536
    index = faiss.IndexFlatL2(dim)

    batch_size = 50
    vectors = []
    MAX_RETRIES = 3

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        print(f"🔄 Embedding batch {i + 1}–{i + len(batch)} / {len(chunks)}", flush=True)

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = embedding_client.embeddings.create(
                    input=batch,
                    model=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT_NAME")
                )
                for r in response.data:
                    vectors.append(np.array(r.embedding, dtype=np.float32))
                print(f"✅ Batch {i + 1}–{i + len(batch)} procesado correctamente.", flush=True)
                break  # salta al siguiente batch si todo sale bien
            except Exception as e:
                print(f"⚠️ Intento {attempt}/{MAX_RETRIES} fallido: {str(e)}", flush=True)
                if attempt < MAX_RETRIES:
                    wait_time = 2 ** attempt
                    print(f"⏳ Esperando {wait_time} segundos antes de reintentar...", flush=True)
                    time.sleep(wait_time)
                else:
                    print("❌ Batch omitido por error persistente.")
                    break  # o podés hacer: raise

        time.sleep(1.5)  # para evitar el 429 en general

    vectors = np.array(vectors)
    index.add(vectors)
    faiss.write_index(index, INDEX_FILE)
    np.save(CHUNKS_FILE, chunks)
    print("✅ Index built and saved.", flush=True)


def load_faiss_index():
    index = faiss.read_index(INDEX_FILE)
    chunks = np.load(CHUNKS_FILE, allow_pickle=True)
    return index, chunks


def query_index(user_input, top_k=5):
    index, chunks = load_faiss_index()
    query_vec = embed(user_input).reshape(1, -1)
    _, I = index.search(query_vec, top_k)
    return [chunks[i] for i in I[0]]


def generate_response(user_input):
    context_chunks = query_index(user_input)
    context = "\n\n".join(context_chunks)
    prompt = (
        "Usando la siguiente normativa del GHS:\n\n"
        f"{context}\n\n"
        f"Respondé la siguiente pregunta según esta normativa:\n{user_input}"
    )
    response = chat_client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
