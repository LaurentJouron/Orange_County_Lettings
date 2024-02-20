import pytest
from profiles.models import Profile


@pytest.fixture
def user1(django_user_model):
    return django_user_model.objects.create_user(
        username="test_user1", password="password"
    )


@pytest.fixture
def user2(django_user_model):
    return django_user_model.objects.create_user(
        username="test_user2", password="password"
    )


@pytest.fixture
def profile1_fixture(user1):
    return Profile.objects.create(
        user=user1,
        favorite_city="Dream team city",
    )


@pytest.fixture
def profile2_fixture(user2):
    return Profile.objects.create(
        user=user2,
        favorite_city="Dark team city",
    )
