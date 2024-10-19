from rest_framework import serializers
from products.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

class ProductSerializer(serializers.ModelSerializer):
    sale_price = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[
        MaxValueValidator(Decimal('9999999999.99')),
        MinValueValidator(Decimal('0.00'))
    ])
    discount_percentage = serializers.DecimalField(
        max_digits=3, 
        decimal_places=0,
        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))],
        required=False,
    )

    class Meta:
        model = Product
        fields = ['name', 'rating', 'price', 'on_sale', 'discount_percentage', 'sale_price', 'image_url', 'alt_text']

    def get_sale_price(self, obj):
        if obj.on_sale and obj.discount_percentage:
            return obj.price - (obj.price * obj.discount_percentage / 100)
        return None

    def validate(self, data):
        if data.get('on_sale') and not data.get('discount_percentage'):
            raise serializers.ValidationError({
                'discount_percentage': "O campo 'discount_percentage' é obrigatório quando o produto está em promoção."
            })
        return data
