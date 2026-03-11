from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from django.conf import settings
from azure.search.documents.models import VectorizedQuery


search_client = SearchClient(
    endpoint=settings.AZURE_SEARCH_ENDPOINT,
    index_name=settings.AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(settings.AZURE_SEARCH_KEY)
)


def search_similar(embedding):

    vector_query = VectorizedQuery(
        vector=embedding,
        k_nearest_neighbors=3,
        fields="embedding"
    )

    results = search_client.search(
        search_text="",
        vector_queries=[vector_query],
        select=["content"]
    )

    docs = list(results)

    return [doc["content"] for doc in docs]


def upload_chunks(chunks, embeddings, document_name):

    docs = []

    safe_name = document_name.replace(" ", "_")

    for i, chunk in enumerate(chunks):

        docs.append({
            "id": f"{safe_name}_{i}",
            "content": chunk,
            "embedding": embeddings[i],
            "document": document_name
        })

    search_client.upload_documents(docs)