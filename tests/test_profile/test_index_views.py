# import pytest

# from django.urls import reverse
# from django.test import Client
# from pytest_django.asserts import assertTemplateUsed


# @pytest.mark.django_db
# def test_index_view(user_fixture):
#     client = Client()
#     path = reverse("profiles:index")
#     response = client.get(path)
#     content = response.content.decode()
#     print("content : ", content)
#     expected_content = '<a href="/profiles/test/">test</a>'
#     assert expected_content in content
#     assert response.status_code == 200
#     assertTemplateUsed(response, "profiles/index.html")
