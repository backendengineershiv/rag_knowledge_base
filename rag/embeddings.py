from core.azure_openai import client
from django.conf import settings

def generate_embedding(text):

    response = client.embeddings.create(
        model=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        input=text
    )

    return response.data[0].embedding