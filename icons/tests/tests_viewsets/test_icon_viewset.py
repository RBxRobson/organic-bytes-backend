from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from icons.models import Icon
from icons.serializers import IconSerializer

class IconViewSetTests(APITestCase):

    def setUp(self):
        # Criação de alguns ícones de exemplo
        self.icon1 = Icon.objects.create(image_url="http://example.com/icon1.png", alt="Icon 1")
        self.icon2 = Icon.objects.create(image_url="http://example.com/icon2.png", alt="Icon 2")

        self.valid_data = {
            "image_url": "http://example.com/newicon.png",
            "alt": "New Icon"
        }

        self.invalid_data = {
            "image_url": "",  # Campo inválido, pois está vazio
            "alt": "Invalid Icon"
        }

        # URL para acessar a lista de ícones
        self.list_url = reverse("icon-list")

    def test_list_icons(self):
        """
        Testa a listagem de ícones.
        """
        response = self.client.get(self.list_url)
        icons = Icon.objects.all()
        serializer = IconSerializer(icons, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_valid_icon(self):
        """
        Testa a criação de um ícone válido.
        """
        response = self.client.post(self.list_url, data=self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Icon.objects.count(), 3)  # Deverá ter 3 ícones no total
        self.assertEqual(Icon.objects.last().alt, "New Icon")

    def test_create_invalid_icon(self):
        """
        Testa a criação de um ícone inválido.
        """
        response = self.client.post(self.list_url, data=self.invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Icon.objects.count(), 2)  # Nenhum novo ícone deve ser criado

    def test_update_icon(self):
        """
        Testa a atualização de um ícone existente.
        """
        url = reverse("icon-detail", kwargs={"pk": self.icon1.pk})
        response = self.client.put(url, data={"image_url": "http://example.com/updatedicon.png", "alt": "Updated Icon"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.icon1.refresh_from_db()
        self.assertEqual(self.icon1.image_url, "http://example.com/updatedicon.png")
        self.assertEqual(self.icon1.alt, "Updated Icon")

    def test_delete_icon(self):
        """
        Testa a remoção de um ícone existente.
        """
        url = reverse("icon-detail", kwargs={"pk": self.icon2.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Icon.objects.count(), 1)  # Apenas 1 ícone deve restar após a exclusão
