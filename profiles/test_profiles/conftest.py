"""
Fixtures for profile-related tests.

These fixtures are used to set up sample data for testing profile-related functionality.
"""

import pytest
from profiles.models import Profile


@pytest.fixture
def user1(django_user_model):
    """
    Fixture for creating the first user instance.

    Returns:
        User: A Django user instance.
    """
    return django_user_model.objects.create_user(
        username="test_user1", password="password"
    )


@pytest.fixture
def user2(django_user_model):
    """
    Fixture for creating the second user instance.

    Returns:
        User: A Django user instance.
    """
    return django_user_model.objects.create_user(
        username="test_user2", password="password"
    )


@pytest.fixture
def profile1_fixture(user1):
    """
    Fixture for creating the first profile instance.

    Returns:
        Profile: A Profile instance with sample data.
    """
    return Profile.objects.create(
        user=user1,
        favorite_city="Dream team city",
    )


@pytest.fixture
def profile2_fixture(user2):
    """
    Fixture for creating the second profile instance.

    Returns:
        Profile: A Profile instance with sample data.
    """
    return Profile.objects.create(
        user=user2,
        favorite_city="Dark team city",
    )
