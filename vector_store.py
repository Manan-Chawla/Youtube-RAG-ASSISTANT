import faiss
import numpy as np
import pickle


def create_faiss_index(embeddings):

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)

    vectors = np.array(
        embeddings,
        dtype="float32"
    )

    index.add(vectors)

    return index


def save_index(index, path="faiss_index/index.faiss"):

    faiss.write_index(
        index,
        path
    )


def load_index(path="faiss_index/index.faiss"):

    return faiss.read_index(path)


def save_chunks(
    chunks,
    path="faiss_index/chunks.pkl"
):

    with open(path, "wb") as f:
        pickle.dump(chunks, f)


def load_chunks(
    path="faiss_index/chunks.pkl"
):

    with open(path, "rb") as f:
        return pickle.load(f)