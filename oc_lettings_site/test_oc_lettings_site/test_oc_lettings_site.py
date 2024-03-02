import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve

from django.test import Client

client = Client()


@pytest.mark.django_db
def test_index_url():
    """
    Test the URL mapping for the index view.

    Checks if the URL mapping for the index view ('index') is correct.
    """
    path = reverse("index")
    assert path == "/"
    assert resolve(path).view_name == "index"


@pytest.mark.django_db
def test_index_view():
    """
    Test the index view.

    Checks if the index view ('index') renders correctly and contains expected content.
    """
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    print("content : ", content)
    expected_content = '<h1 class="page-header-ui-title mb-3 display-6">'
    "Welcome to Holiday Homes</h1>"
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
