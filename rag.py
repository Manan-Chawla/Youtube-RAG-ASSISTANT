from google import genai

from config import GOOGLE_API_KEY
from retriever import retrieve

client = genai.Client(
    api_key=GOOGLE_API_KEY
)


def ask_question(question):

    chunks = retrieve(
        question,
        k=3
    )

    context = "\n\n".join(chunks)

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is unavailable,
say:

I could not find that information in the video.

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text