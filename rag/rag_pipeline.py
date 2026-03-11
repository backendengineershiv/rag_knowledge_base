from .embeddings import generate_embedding
from .vector_store import search_similar
from core.azure_openai import client
from django.conf import settings


def answer_question(question):

    query_embedding = generate_embedding(question)

    contexts = search_similar(query_embedding)

    context_text = "\n".join(contexts)

    prompt = f"""
        Use the context below to answer the question.

        Context:
        {context_text}

        Question:
        {question}
    """

    response = client.chat.completions.create(
        model=settings.AZURE_OPENAI_CHAT_DEPLOYMENT,
        messages=[
            {"role": "system", "content": "Answer using the provided context."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content