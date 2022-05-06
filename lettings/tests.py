from django.test import TestCase
from django.urls import reverse

from lettings.models import Letting, Address


class LettingsTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street="",
            city="",
            state="",
            zip_code=2,
            country_iso_code=""
        )
        self.letting = Letting.objects.create(title="Test Title", address=self.address)

    def test_lettings_index(self):
        response = self.client.get(reverse("lettings:index"))
        assert response.status_code == 200
        self.assertContains(response, "<title>Lettings</title>")
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_lettings_title(self):
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
        assert response.status_code == 200
        self.assertContains(response, "<title>Test Title</title>")
