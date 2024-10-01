from rest_framework import viewsets
from home.models import Hero
from home.serializers import HeroSerializer

# Definição da ViewSet para o modelo Hero
class HeroViewSet(viewsets.ModelViewSet):
    # Recupera todos os registros de Hero
    queryset = Hero.objects.all()  
    
    # Serializador que será usado para manipular os dados do modelo
    serializer_class = HeroSerializer  
