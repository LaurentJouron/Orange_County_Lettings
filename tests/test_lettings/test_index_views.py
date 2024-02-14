import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_index_view():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "lettings_list" in response.context


@pytest.mark.django_db
def test_index_view_no_lettings():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 404
