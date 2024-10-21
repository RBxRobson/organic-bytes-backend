from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from decimal import Decimal
from products.models import Product

class ProductViewSetTest(APITestCase):
    
    def setUp(self):
        # Produto básico para testes
        self.product = Product.objects.create(
            name="Produto Teste",
            rating=4,
            price=Decimal('100.00'),
            image_url="http://example.com/image.png",
            alt_text="Texto Alternativo"
        )
        self.url = reverse('product-list')

    def test_create_product_success(self):
        """Testa a criação de um produto com sucesso"""
        data = {
            'name': 'Novo Produto',
            'rating': 5,
            'price': '200.00',
            'on_sale': True,
            'discount_percentage': 10,
            'image_url': 'http://example.com/new-image.png',
            'alt_text': 'Alt text exemplo'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Novo Produto')
        self.assertEqual(Decimal(response.data['price']), Decimal('200.00'))
        self.assertEqual(response.data['sale_price'], Decimal('180.00')) 

    def test_create_product_without_discount_fails(self):
        """Testa a criação de um produto em promoção sem desconto"""
        data = {
            'name': 'Produto Sem Desconto',
            'rating': 4,
            'price': '150.00',
            'on_sale': True,
            'image_url': 'http://example.com/no-discount-image.png',
            'alt_text': 'Alt text exemplo'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Verifica se o campo 'discount_percentage' contém o erro esperado
        self.assertIn('discount_percentage', response.data)
        self.assertEqual(
            response.data['discount_percentage'][0],
            "O campo 'discount_percentage' é obrigatório quando o produto está em promoção."
    )


    def test_update_product_success(self):
        """Testa a atualização de um produto existente"""
        url = reverse('product-detail', args=[self.product.id])
        data = {
            'name': 'Produto Atualizado',
            'rating': 5,
            'price': '300.00',
            'on_sale': True,
            'discount_percentage': 20,
            'image_url': 'http://example.com/updated-image.png',
            'alt_text': 'Alt text atualizado'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Produto Atualizado')
        self.assertEqual(response.data['sale_price'], Decimal('240.00')) 

    def test_list_products(self):
        """Testa a listagem de produtos"""
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  

    def test_delete_product(self):
        """Testa a exclusão de um produto"""
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())  
