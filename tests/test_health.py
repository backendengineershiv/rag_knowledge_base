import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_api_running():

    client = APIClient()

    response = client.get("/")

    assert response.status_code in [200, 404]