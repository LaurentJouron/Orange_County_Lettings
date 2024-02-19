import pytest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.fixture
def fake_profile_fixture():
    return [
        Profile(
            id="1",
            favorite_city="Buenos Aires",
            user_id="5",
        ),
        Profile(
            id="2",
            favorite_city="Barcelona",
            user_id="4",
        ),
        Profile(
            id="3",
            favorite_city="Budapest",
            user_id="3",
        ),
        Profile(
            id="4",
            favorite_city="Berlin",
            user_id="2",
        ),
    ]


@pytest.fixture
def profile_fixture(monkeypatch, fake_profile_fixture):
    monkeypatch.setattr(
        "profiles.models.Profile",
        lambda: fake_profile_fixture,
    )
    return {"profile": fake_profile_fixture}


@pytest.fixture
def user_fixture(django_user_model):
    return django_user_model.objects.create_user(
        username="test", password="password"
    )


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
        assert "La page demandée n'existe pas" in response.content.decode(
            "utf-8"
        )
