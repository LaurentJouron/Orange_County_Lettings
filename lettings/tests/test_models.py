import pytest
from django.urls import reverse
from lettings.models import Address, Letting

from django.test import Client


@pytest.mark.django_db
def test_address_model():
    address = Address.objects.create(
        number=500,
        street="Dream Avenue",
        city="Dream city",
        state="LA",
        zip_code=10000,
        country_iso_code="USA",
    )
    expected_value = "500 Dream Avenue"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_index_view():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "lettings_list" in response.context


@pytest.mark.django_db
def test_letting_view():
    letting = Letting.objects.create(
        title="Test Letting", address="Test Address"
    )
    client = Client()
    response = client.get(
        reverse("letting", kwargs={"letting_id": letting.id})
    )
    assert response.status_code == 200
    assert "title" in response.context
    assert "address" in response.context


@pytest.mark.django_db
def test_index_view_no_lettings():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 404


@pytest.mark.django_db
def test_letting_view_not_found():
    client = Client()
    response = client.get(reverse("letting", kwargs={"letting_id": 999}))
    assert response.status_code == 404
