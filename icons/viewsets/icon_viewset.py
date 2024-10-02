from rest_framework import viewsets
from icons.models import Icon
from icons.serializers import IconSerializer

# Definição da ViewSet para o modelo Icon
class IconViewSet(viewsets.ModelViewSet):
    # Recupera todos os registros de Icon
    queryset = Icon.objects.all()  
    
    # Serializador que será usado para manipular os dados do modelo
    serializer_class = IconSerializer  
