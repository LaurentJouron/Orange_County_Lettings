import pytest
from django.test import Client
from lettings.models import Address

client = Client()


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
