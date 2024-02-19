from django.test import TestCase, Client

from django.contrib.auth.models import User
from profiles.models import Profile
import pytest

from django.urls import reverse, resolve


@pytest.mark.django_db
def test_index_url(profile_fixture):
    profile_fixture
    path = reverse("profiles:index")
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"


@pytest.mark.django_db
def test_profile_url(profile_fixture):
    profile_fixture
    path = reverse("profiles:profile", kwargs={"username": "test"})
    assert path == "/profiles/test/"
    assert resolve(path).view_name == "profiles:profile"


@pytest.mark.django_db
def test_profile_model(user_fixture):
    profile = Profile.objects.create(
        user=user_fixture,
        favorite_city="Very big city",
    )
    expected_value = "test"
    assert str(profile) == expected_value


class TestProfiles(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(
            id=666,
            username="MrRobot",
        )
        Profile.objects.create(
            id=666,
            favorite_city="Rouen",
            user_id=666,
        )

    def test_access_homepage(self):
        response = self.client.get("/profiles/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Profiles" in response.content.decode("utf-8")

    def test_access_existing_profile(self):
        response = self.client.get("/profiles/MrRobot", follow=True)
        output = response.status_code
        expected = 200
        assert output == expected
        assert "MrRobot" in response.content.decode("utf-8")

    def test_access_unexisting_profile(self):
        response = self.client.get("/profiles/Cedric_Delauney")
        output = response.status_code
        expected = 301
        assert output == expected

    def test_access_unexisting_profile_page(self):
        response = self.client.get("/profiles2")
        output = response.status_code
        expected = 404
        assert output == expected
