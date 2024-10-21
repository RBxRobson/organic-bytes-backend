import pytest
from products.models import Product
from products.serializers import ProductSerializer
from decimal import Decimal

@pytest.mark.django_db
class TestProductSerializer:

    def test_valid_product_creation(self):
        data = {
            'name': 'Produto Teste',
            'rating': 4,
            'price': '100.00',
            'on_sale': True,
            'discount_percentage': 10,
            'image_url': 'http://example.com/image.png',
            'alt_text': 'Alt text exemplo'
        }
        serializer = ProductSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        product = serializer.save()
        assert serializer.validated_data['price'] == Decimal('100.00')
        sale_price = serializer.get_sale_price(product)
        assert sale_price == Decimal('90.00')


    def test_discount_percentage_required_on_sale(self):
        data = {
            'name': 'Produto Sem Desconto',
            'rating': 3,
            'price': '150.00',
            'on_sale': True,
            'image_url': 'http://example.com/image.png',
            'alt_text': 'Alt text exemplo'
        }
        serializer = ProductSerializer(data=data)
        assert not serializer.is_valid()
        assert 'discount_percentage' in serializer.errors

    def test_no_sale_price_when_not_on_sale(self):
        data = {
            'name': 'Produto Sem Promoção',
            'rating': 5,
            'price': '200.00',
            'on_sale': False,
            'image_url': 'http://example.com/image.png',
            'alt_text': 'Alt text exemplo'
        }
        serializer = ProductSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        product = serializer.save()
        sale_price = serializer.get_sale_price(product)
        assert sale_price is None


