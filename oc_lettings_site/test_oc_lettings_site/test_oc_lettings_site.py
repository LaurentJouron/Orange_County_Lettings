import pytest
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed
from django.test import Client, TestCase

client = Client()


@pytest.mark.django_db
def test_index_url():
    path = reverse("index")
    assert path == "/"
    assert resolve(path).view_name == "index"


@pytest.mark.django_db
def test_index_view():
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = '<h1 class="page-header-ui-title mb-3 display-6">'
    "Welcome to Holiday Homes</h1>"
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


class TestOcLettingsSite(TestCase):

    def setUp(self):
        self.client = Client()

    def test_access_homepage(self):
        response = self.client.get("/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Welcome" in response.content.decode("utf-8")

    def test_access_unavailable_page(self):
        response = self.client.get("/unavailable_page")
        output = response.status_code
        expected = 404
        assert output == expected
