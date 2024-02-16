# import pytest
# from django.urls import reverse, resolve
# from lettings.models import Letting
# from django.test import Client

# client = Client()


# @pytest.mark.django_db
# def test_index_url(address_fixture):
#     Letting.objects.create(title="The dream place", address=address_fixture)
#     Letting.objects.create(title="The dark place", address=address_fixture)
#     path = reverse("lettings:index")
#     assert path == "/lettings/"
#     assert resolve(path).view_name == "lettings:index"
