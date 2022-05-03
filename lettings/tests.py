from django.test import TestCase
from django.urls import reverse

from lettings.models import Letting, Address


class LettingsTest(TestCase):
    def setUp(self):
        self.letting = Letting.objects.create()

    def test_lettings_index(self):
        response = self.client.get(reverse("lettings:index"))
        assert response.status_code == 200
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_lettings_title(self):
        response = self.client.get(reverse("lettings:letting", args=[self.request]))
