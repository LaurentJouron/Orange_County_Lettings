# import pytest
# from django.urls import reverse
# from django.test import Client


# @pytest.mark.django_db
# def test_letting_view_not_found():
#     client = Client()
#     response = client.get(reverse("letting", kwargs={"letting_id": 999}))
#     assert response.status_code == 404
