from rest_framework.serializers import ModelSerializer
from .models import Bus, Location

class BusSerializer(ModelSerializer):
    class Meta:
        model=Bus
        fields='__all__'

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'