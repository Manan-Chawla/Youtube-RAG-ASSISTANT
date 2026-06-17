import os

from transcript import get_transcript
from chunking import chunk_text
from embeddings import create_embeddings

from vector_store import (
    create_faiss_index,
    save_index,
    save_chunks
)


def ingest_video(url):

    text = get_transcript(url)

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    index = create_faiss_index(embeddings)

    os.makedirs("data", exist_ok=True)

    save_index(index, "data/index.faiss")

    save_chunks(chunks, "data/chunks.pkl")

    return len(chunks)