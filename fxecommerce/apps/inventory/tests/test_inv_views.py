import pytest
from django.test import Client

@pytest.mark.django_db
def test_employee():
    client = Client()
    response = client.get('/employee/')
    assert response.status_code == 200
