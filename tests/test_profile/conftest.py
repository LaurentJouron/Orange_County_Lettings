import pytest
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
