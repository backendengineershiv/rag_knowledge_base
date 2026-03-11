from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import DocumentSerializer
from .services import extract_text
from rag.rag_pipeline import answer_question
from rag.chunking import split_text
from rag.embeddings import generate_embedding
from rag.vector_store import upload_chunks


class UploadDocumentView(APIView):

    def post(self, request):

        serializer = DocumentSerializer(data=request.data)

        if serializer.is_valid():

            doc = serializer.save()

            text = extract_text(doc.file.path)

            chunks = split_text(text)

            embeddings = [generate_embedding(chunk) for chunk in chunks]

            upload_chunks(chunks, embeddings, doc.title)

            return Response({"message": "Document indexed"})

        return Response(serializer.errors)
    



class AskQuestionView(APIView):

    def post(self, request):

        question = request.data.get("question")

        answer = answer_question(question)

        return Response({
            "question": question,
            "answer": answer
        })