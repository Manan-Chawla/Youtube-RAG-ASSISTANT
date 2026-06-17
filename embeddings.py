from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)


def get_embedding(text):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def create_embeddings(chunks):

    embeddings = []

    for chunk in chunks:
        vector = get_embedding(chunk)
        embeddings.append(vector)

    return embeddings