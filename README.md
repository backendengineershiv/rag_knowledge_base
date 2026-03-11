# RAG Knowledge Base API

A production-style Retrieval-Augmented Generation (RAG) backend built using:

- Django REST Framework
- Azure OpenAI
- Azure AI Search
- Vector embeddings

## Features

- Upload documents (PDF)
- Automatic text extraction
- Text chunking
- Embedding generation
- Vector search using Azure AI Search
- Question answering with GPT-4.1

## Architecture

User Upload
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings (Azure OpenAI)
    ↓
Azure AI Search (Vector DB)
    ↓
User Question
    ↓
Vector Retrieval
    ↓
GPT-4.1 Response

## Setup

### Clone repository

git clone git@github.com:backendengineershiv/rag_knowledge_base.git

cd rag-knowledge-base

### Install dependencies

pip install -r requirements.txt

### Create .env

AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=your_endpoint

AZURE_SEARCH_ENDPOINT=your_search_endpoint
AZURE_SEARCH_KEY=your_search_key

### Run server

python manage.py runserver

## API Endpoints

### Upload document

POST /api/upload/

### Ask question

POST /api/ask/

## Run with Docker

Build image:

docker build -t rag-api .

Run container:

docker run -p 8000:8000 rag-api

## Run with Docker Compose

docker compose up
--------------------------------------------------------------------
Pull the Docker image from Docker Hub:

docker pull shivpratapraj/rag-api

Run the container:

docker run -p 8001:8000 --env-file .env shivpratapraj/rag-api

The API will be available at:

http://localhost:8001
Also Add a Note About .env

Since your project uses Azure credentials, explain this.

Example:

Environment Variables

Create a .env file with the following variables:

AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=your_endpoint

AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4.1
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-large

AZURE_SEARCH_ENDPOINT=your_search_endpoint
AZURE_SEARCH_KEY=your_search_key
AZURE_SEARCH_INDEX=rag-documents