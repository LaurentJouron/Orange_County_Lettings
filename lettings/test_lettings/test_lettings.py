import pytest

from django.test import TestCase, Client
from lettings.models import Address, Letting


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


class TestLettings(TestCase):

    def setUp(self):

        self.client = Client()
        Address.objects.create(
            id=666,
            number=666,
            zip_code=666,
        )
        Letting.objects.create(
            id=666, title="Joshua Tree Green Haus", address_id=666
        )

    def test_access_homepage(self):
        response = self.client.get("/lettings/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Lettings" in response.content.decode("utf-8")

    def test_access_existing_letting(self):
        response = self.client.get("/lettings/666", follow=True)
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Joshua Tree Green Haus" in response.content.decode("utf-8")

    def test_access_unexisting_letting(self):
        response = self.client.get("/lettings/6666666")
        output = response.status_code
        expected = 301
        assert output == expected

    def test_access_unavailable_letting_page(self):
        response = self.client.get("/lettings2")
        output = response.status_code
        expected = 404
        assert output == expected
