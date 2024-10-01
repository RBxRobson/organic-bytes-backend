from rest_framework import serializers
from home.models import Hero

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = [
            'id', 
            'image_url', 
            'title', 
            'subtitle', 
            'description', 
            'highlighted_text'
        ]
