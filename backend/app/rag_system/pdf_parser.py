import fitz  # PyMuPDF


def extract_chunks_from_pdf(pdf_path, max_chars=1000):
    doc = fitz.open(pdf_path)
    chunks = []
    for page in doc:
        text = page.get_text()
        for i in range(0, len(text), max_chars):
            chunk = text[i:i + max_chars].strip()
            if len(chunk) > 100:
                chunks.append(chunk)
    return chunks
