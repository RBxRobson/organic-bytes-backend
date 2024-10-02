import factory
from icons.models import Icon

class IconFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Icon

    id = factory.Faker('random_int', min=1, max=1000)
    
    # Gera um link para uma imagem aleatória
    image_url = factory.Faker('image_url')  
    
    # Gera uma frase aleatória como descrição do icone
    alt = factory.Faker('sentence', nb_words=8)  

