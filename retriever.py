import numpy as np

from embeddings import get_embedding

from vector_store import (
    load_index,
    load_chunks
)


def retrieve(
    query,
    k=3
):

    index = load_index(
    "data/index.faiss"
)

    chunks = load_chunks(
    "data/chunks.pkl"
)

    query_embedding = get_embedding(
        query
    )

    query_vector = np.array(
        [query_embedding],
        dtype="float32"
    )

    distances, indices = index.search(
        query_vector,
        k
    )

    results = []

    for idx in indices[0]:
        results.append(
            chunks[idx]
        )

    return results