# from django.test import TestCase, RequestFactory
# from django.urls import reverse
# from django.http import Http404
# from unittest.mock import patch
# from lettings.models import Letting
# from lettings.views import index, letting


# class LettingViewsTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#     def test_index_view_with_no_lettings(self):
#         request = self.factory.get(reverse("index"))
#         with patch("lettings.views.Letting.objects.all") as mock_lettings_all:
#             mock_lettings_all.return_value = []
#             with self.assertRaises(Http404):
#                 index(request)

#     def test_index_view_with_lettings(self):
#         let1 = Letting.objects.create(title="Test1", address="Address1")
#         let2 = Letting.objects.create(title="Test2", address="Address2")
#         request = self.factory.get(reverse("index"))
#         response = index(request)
#         self.assertContains(response, let1.title)
#         self.assertContains(response, let1.address)
#         self.assertContains(response, let2.title)
#         self.assertContains(response, let2.address)

#     def test_letting_view_with_existing_letting(self):
#         letting = Letting.objects.create(title="Test1", address="Address1")
#         request = self.factory.get(reverse("letting", args=[letting.id]))
#         response = letting(request, letting.id)
#         self.assertContains(response, letting.title)
#         self.assertContains(response, letting.address)

#     def test_letting_view_with_nonexistent_letting(self):
#         request = self.factory.get(reverse("letting", args=[999]))
#         with self.assertRaises(Http404):
#             letting(request, 999)
