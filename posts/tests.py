from django.test import TestCase
from django.urls import reverse


class VistasTest(TestCase):
    def test_inicio(self):
        response = self.client.get(reverse("inicio"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/inicio.html")

    def test_acerca(self):
        response = self.client.get(reverse("acerca"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/acerca.html")