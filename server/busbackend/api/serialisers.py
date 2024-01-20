from rest_framework.serializers import ModelSerializer
from .models import *

class BusSerializer(ModelSerializer):
    class Meta:
        model=Bus
        fields='__all__'

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
class RoutesSerializer(ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'