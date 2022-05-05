from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import models
from profiles.models import Profile


class ProfilesTest(TestCase):
    def setUp(self):
        self.user = models.User.objects.create(
            username="Test_username",
            first_name="Dummy first_name",
            last_name="Dummy last_name",
            email="Dummy@email",
        )
        self.profile = Profile.objects.create(favorite_city="Test City", user=self.user)

    def test_profiles_index(self):
        response = self.client.get(reverse("profiles:index"))
        assert response.status_code == 200
        self.assertContains(response, "<title>Profiles</title>")
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_profiles_title(self):
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        assert response.status_code == 200
        self.assertContains(response, "Test City")

    def test_profiles_user_content(self):
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        self.assertContains(response, "Dummy first_name")
        self.assertContains(response, "Dummy last_name")
        self.assertContains(response, "Dummy@email")
