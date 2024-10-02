import pytest
from icons.serializers import IconSerializer
from icons.factories import IconFactory

@pytest.mark.django_db
def test_icon_serializer():
    # Cria uma instância de icon usando a factory
    icon = IconFactory()

    # Serializa a instância de icon
    serializer = IconSerializer(icon)

    # Verifica se os dados serializados estão corretos
    assert serializer.data['id'] == icon.id
    assert serializer.data['image_url'] == icon.image_url
    assert serializer.data['alt'] == icon.alt