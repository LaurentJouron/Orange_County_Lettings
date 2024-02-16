# import pytest
# from django.urls import reverse, resolve
# from lettings.models import Letting
# from django.test import Client

# client = Client()


# @pytest.mark.django_db
# def test_letting_url(address_fixture):
#     Letting.objects.create(title="The dream place", address=address_fixture)
#     path = reverse("lettings:letting", kwargs={"letting_id": 1})

#     assert path == "/lettings/1/"
#     assert resolve(path).view_name == "lettings:letting"
