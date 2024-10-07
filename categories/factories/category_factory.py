import factory
from categories.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    image_url = factory.Faker('url')
    alt = factory.Faker('sentence', nb_words=4)
    name = factory.Faker('word')
