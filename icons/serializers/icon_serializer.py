from rest_framework import serializers
from icons.models import Icon

class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = [
            'id', 
            'image_url', 
            'alt'
        ]
