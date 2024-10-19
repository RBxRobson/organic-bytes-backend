import factory
from faker import Faker
from products.models import Product

fake = Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    rating = factory.Faker('random_int', min=0, max=5)
    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    image_url = factory.Faker('image_url')
    alt_text = factory.Faker('sentence', nb_words=6)
    on_sale = factory.Faker('boolean') 
    discount_percentage = factory.Maybe(
        'on_sale',
        factory.Faker('random_int', min=0, max=100),
    )

    @factory.lazy_attribute
    def sale_price(self):
        if self.on_sale and self.discount_percentage:
            return self.price - (self.price * self.discount_percentage / 100)
        return None
