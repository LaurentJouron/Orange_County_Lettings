import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve
from django.test import Client
from bs4 import BeautifulSoup

from lettings.models import Address, Letting

client = Client()


@pytest.mark.django_db
def test_address_model():
    """
    Test the __str__() method of the Address model.

    Checks if the textual representation of an Address instance is correct.
    """
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
def test_letting_model():
    """
    Test the __str__() method of the Letting model.

    Checks if the textual representation of a Letting instance is correct.
    """
    address = Address.objects.create(
        number=500,
        street="Dream Avenue",
        city="Dream city",
        state="LA",
        zip_code=10000,
        country_iso_code="USA",
    )
    letting = Letting.objects.create(title="The dream place", address=address)

    expected_value = "The dream place"
    assert str(letting) == expected_value


@pytest.mark.django_db
def test_index_url(address1_fixture, address2_fixture):
    """
    Test the URL mapping for the index view.

    Checks if the URL mapping for the index view ('lettings:index') is correct.
    """
    Letting.objects.create(title="The dream place", address=address1_fixture)
    Letting.objects.create(title="The dark place", address=address2_fixture)
    path = reverse("lettings:index")
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


@pytest.mark.django_db
def test_letting_url(address1_fixture):
    """
    Test the URL mapping for the letting view.

    Checks if the URL mapping for the letting view ('lettings:letting') is correct.
    """
    Letting.objects.create(title="The dream place", address=address1_fixture)
    path = reverse("lettings:letting", kwargs={"letting_id": 1})

    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"


@pytest.mark.django_db
def test_index_view(address1_fixture, address2_fixture):
    """
    Test the index view.

    Checks if the index view ('lettings:index') renders correctly and contains expected content.
    """
    Letting.objects.create(title="The dream place", address=address1_fixture)
    Letting.objects.create(title="The dark place", address=address2_fixture)
    path = reverse("lettings:index")
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")
    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.find("a", href="/lettings/1/").text == "The dream place"


@pytest.mark.django_db
def test_letting_view(address1_fixture):
    """
    Test the letting view.

    Checks if the letting view ('lettings:letting') renders correctly and contains expected content.
    """
    Letting.objects.create(title="The dream place", address=address1_fixture)
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.find("p").text == "500 Dream Avenue"
