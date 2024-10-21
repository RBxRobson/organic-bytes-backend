from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        # Validação customizada para promoções durante a criação
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Verifica a promoção e aplica o desconto se necessário
        if serializer.validated_data.get('on_sale') and not serializer.validated_data.get('discount_percentage'):
            return Response(
                {"error": "O campo 'discount_percentage' é obrigatório quando o produto está em promoção."},
                status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # Validação customizada para promoções durante a atualização
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Verifica a promoção e aplica o desconto se necessário
        if serializer.validated_data.get('on_sale') and not serializer.validated_data.get('discount_percentage'):
            return Response(
                {"error": "O campo 'discount_percentage' é obrigatório quando o produto está em promoção."},
                status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # Garante que o `clean` do modelo seja chamado
        serializer.save()

    def perform_update(self, serializer):
        # Garante que o `clean` do modelo seja chamado na atualização
        serializer.save()
