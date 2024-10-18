from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=255)  
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    image_url = models.URLField(max_length=500)  
    alt_text = models.CharField(max_length=255)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True, 
        null=True
    )
    discount_percentage = models.DecimalField(
        max_digits=3, 
        decimal_places=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        blank=True, 
        null=True
    )

    def clean(self):
        if self.on_sale and (self.discount_percentage is None):
            raise ValidationError(
                "O campo 'discount_percentage' é obrigatório quando o produto está em promoção."
            )
        if self.on_sale and self.discount_percentage:
            self.sale_price = self.price - (
                self.price * self.discount_percentage / 100
            )
        else:
            self.sale_price = None 

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
