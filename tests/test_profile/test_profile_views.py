# import pytest

# from django.urls import reverse
# from django.test import Client
# from pytest_django.asserts import assertTemplateUsed


# @pytest.mark.django_db
# def test_profile_view(profile_fixture):
#     client = Client()
#     profile_fixture
#     path = reverse("profiles:profile", kwargs={"username": "test"})
#     response = client.get(path)
#     content = response.content.decode()
#     print("content : ", content)
#     expected_content = "Dream team city"
#     assert expected_content in content
#     assert response.status_code == 200
#     assertTemplateUsed(response, "profiles/profile.html")
