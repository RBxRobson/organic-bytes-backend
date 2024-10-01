import factory
from home.models import Hero

class HeroFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hero

    id = factory.Faker('random_int', min=1, max=1000)
    
    # Gera um link para uma imagem aleatória
    image_url = factory.Faker('image_url')  
    
    # Gera uma frase aleatória como título
    title = factory.Faker('sentence', nb_words=4)  
    
    # Gera uma frase aleatória como subtítulo
    subtitle = factory.Faker('sentence', nb_words=6)  
    
    # Gera um parágrafo como descrição
    description = factory.Faker('paragraph')  
    
    # Palavra aleatória destacada
    highlighted_text = factory.Faker('word')  
