import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve
from django.test import Client

from lettings.models import Address, Letting

client = Client()


@pytest.mark.django_db
def test_adress_model():
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
    Letting.objects.create(title="The dream place", address=address1_fixture)
    Letting.objects.create(title="The dark place", address=address2_fixture)
    path = reverse("lettings:index")
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


@pytest.mark.django_db
def test_letting_url(address1_fixture):
    Letting.objects.create(title="The dream place", address=address1_fixture)
    path = reverse("lettings:letting", kwargs={"letting_id": 1})

    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"


@pytest.mark.django_db
def test_index_view(address1_fixture, address2_fixture):
    Letting.objects.create(title="The dream place", address=address1_fixture)
    Letting.objects.create(title="The dark place", address=address2_fixture)
    path = reverse("lettings:index")
    response = client.get(path)
    content = response.content.decode()
    print("content : ", content)
    expected_content = '<a href="/lettings/1/">The dream place</a>'
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_view(address1_fixture):
    Letting.objects.create(title="The dream place", address=address1_fixture)
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    response = client.get(path)
    content = response.content.decode()
    print("content : ", content)
    expected_content = "<p>500 Dream Avenue</p>"
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
