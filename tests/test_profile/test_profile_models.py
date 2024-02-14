import pytest

from profiles.models import Profile


@pytest.mark.django_db
def test_profile_model(user_fixture):
    profile = Profile.objects.create(
        user=user_fixture,
        favorite_city="Very big city",
    )
    expected_value = "test"
    assert str(profile) == expected_value
