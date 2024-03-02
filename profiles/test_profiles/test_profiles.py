import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve
from django.test import Client
from bs4 import BeautifulSoup

from profiles.models import Profile

client = Client()


@pytest.mark.django_db
def test_profile_model(user1):
    """
    Test the __str__() method of the Profile model.

    Checks if the textual representation of a Profile instance is correct.

    Args:
        user1: Instance of the Django user used to create the profile.
    """
    profile = Profile.objects.create(
        user=user1,
        favorite_city="Very big city",
    )
    expected_value = "test_user1"
    assert str(profile) == expected_value


@pytest.mark.django_db
def test_index_url(profile1_fixture, profile2_fixture):
    """
    Test the URL mapping for the index view.

    Checks if the URL mapping for the index view ('profiles:index') is correct.

    Args:
        profile1_fixture: Fixture representing a Profile instance.
        profile2_fixture: Fixture representing another Profile instance.
    """
    path = reverse("profiles:index")
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"


@pytest.mark.django_db
def test_profile_url(profile1_fixture):
    """
    Test the URL mapping for the profile view.

    Checks if the URL mapping for the profile view ('profiles:profile') is correct.

    Args:
        profile1_fixture: Fixture representing a Profile instance.
    """
    path = reverse("profiles:profile", kwargs={"username": "test_user1"})
    assert path == "/profiles/test_user1/"
    assert resolve(path).view_name == "profiles:profile"


@pytest.mark.django_db
def test_index_view(profile1_fixture, profile2_fixture):
    """
    Test the index view.

    Checks if the index view ('profiles:index') renders correctly and contains expected content.

    Args:
        profile1_fixture: Fixture representing a Profile instance.
        profile2_fixture: Fixture representing another Profile instance.
    """
    path = reverse("profiles:index")
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")
    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.find("a", href="/profiles/test_user2/").text == "test_user2"


@pytest.mark.django_db
def test_profile_view(profile1_fixture):
    """
    Test the profile view.

    Checks if the profile view ('profiles:profile') renders correctly and contains expected content.

    Args:
        profile1_fixture: Fixture representing a Profile instance.
    """
    path = reverse("profiles:profile", kwargs={"username": "test_user1"})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Dream team city"
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
