import pytest
from django.urls import reverse, resolve


@pytest.mark.django_db
def test_profile_url(profile_fixture):
    profile_fixture
    path = reverse("profiles:profile", kwargs={"username": "test"})
    assert path == "/profiles/test/"
    assert resolve(path).view_name == "profiles:profile"
