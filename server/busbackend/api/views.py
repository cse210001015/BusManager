from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *

from .serialisers import *
import json


@api_view(['GET'])
def getRoutes(request):
    routes=[{'Endpoint':'/notes','method':'GET','body':None,'description':'Returns an array of notes'}]
    return Response(routes)

class adminBusesViews(APIView):
    def get(self, request):
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        newBus = Bus.objects.create(**body)
        serializer = BusSerializer(newBus, many= False)
        return Response(serializer.data)
    
class adminBusViews(APIView):
    def get(self, request, pk):
        bus = Bus.objects.get(id = pk)
        serializer = BusSerializer(bus)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        updateBus = Bus.objects.get(id = pk)
        for key in body:
            setattr(updateBus, key, body[key])
        updateBus.save()
        serializer = BusSerializer(updateBus)
        return Response(serializer.data)

    def delete(self, request, pk):
        deleteBus = Bus.objects.get(id = pk).delete()
        return Response(deleteBus[0])

class adminLocationsViews(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        newLocation = Location.objects.create(**body)
        serializer = LocationSerializer(newLocation)
        return Response(serializer.data)

class adminLocationViews(APIView):
    def get(self, request, pk):
        location = Location.objects.get(id = pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        updateLocation = Location.objects.get(id = pk)
        for key in body:
            setattr(updateLocation, key, body[key])
        updateLocation.save()
        serializer = LocationSerializer(updateLocation)
        return Response(serializer.data)

    def delete(self, request, pk):
        deleteLocation = Location.objects.get(id = pk).delete()
        return Response(deleteLocation[0])

class adminRoutesViews(APIView):
    def get(self, request):
        routes = Routes.objects.all()
        serializer = RoutesSerializer(routes, many=True)
        return Response(serializer.data)