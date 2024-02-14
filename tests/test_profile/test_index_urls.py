import pytest
from django.urls import reverse, resolve


@pytest.mark.django_db
def test_index_url(profile_fixture):
    profile_fixture
    path = reverse("profiles:index")
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"
