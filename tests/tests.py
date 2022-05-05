from django.test import TestCase


def test_dummy():
    assert 1


class HomeTests(TestCase):
    def test_home_index(self):
        request = self.client.get("")
        # request = self.client.get(reverse("oc:index"))
        assert request.status_code == 200
        self.assertContains(request, "Welcome to Holiday Homes")
        self.assertContains(request, "<title>Holiday Homes</title>")
