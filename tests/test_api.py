import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_ask_endpoint():

    client = APIClient()

    data = {
        "question": "What is machine learning?"
    }

    response = client.post("/api/ask/", data, format="json")

    assert response.status_code in [200, 400]