from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from home.models import Hero

class HeroViewSetTests(APITestCase):
    def setUp(self):
        # URL base para os testes
        self.list_url = reverse("banners-list")
        
        # Dados válidos para a criação de um herói
        self.valid_data = {
            "image_url": "https://example.com/banner1.jpg",
            "title": "Banner 1",
            "subtitle": "Subtítulo do Banner 1",
            "description": "Descrição do Banner 1",
            "highlighted_text": "Texto em destaque do Banner 1"
        }

        # Criando um herói existente para testes de atualização e exclusão
        self.hero = Hero.objects.create(**self.valid_data)

    def test_list_heroes(self):
        """
        Testa a listagem de heróis.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Deve retornar um herói

    def test_create_valid_banner(self):
        """
        Testa a criação de um banner válido.
        """
        response = self.client.post(self.list_url, data=self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_banner(self):
        """
        Testa a criação de um banner inválido (sem título).
        """
        invalid_data = self.valid_data.copy()
        invalid_data['title'] = ''  # Título vazio
        response = self.client.post(self.list_url, data=invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_banner(self):
        """
        Testa a atualização de um banner existente.
        """
        url = reverse("banners-detail", kwargs={"pk": self.hero.pk})
        response = self.client.put(url, data={
            "image_url": "https://example.com/banner-atualizado.jpg",
            "title": "Banner Atualizado",
            "subtitle": "Novo Subtítulo",
            "description": "Nova descrição",
            "highlighted_text": "Novo texto em destaque"
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.hero.refresh_from_db()  # Atualiza a instância do objeto
        self.assertEqual(self.hero.title, "Banner Atualizado")


    def test_delete_banner(self):
        """
        Testa a exclusão de um banner existente.
        """
        url = reverse("banners-detail", kwargs={"pk": self.hero.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Hero.objects.filter(pk=self.hero.pk).exists())  # Verifica se o herói foi excluído
