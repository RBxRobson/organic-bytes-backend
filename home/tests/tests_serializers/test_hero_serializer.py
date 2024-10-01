import pytest
from home.serializers import HeroSerializer
from home.factories import HeroFactory

@pytest.mark.django_db
def test_hero_serializer():
    # Cria uma instância de Hero usando a factory
    hero = HeroFactory()

    # Serializa a instância de Hero
    serializer = HeroSerializer(hero)

    # Verifica se os dados serializados estão corretos
    assert serializer.data['id'] == hero.id
    assert serializer.data['image_url'] == hero.image_url
    assert serializer.data['title'] == hero.title
    assert serializer.data['subtitle'] == hero.subtitle
    assert serializer.data['description'] == hero.description
    assert serializer.data['highlighted_text'] == hero.highlighted_text
