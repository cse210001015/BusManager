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
    def post(self, request):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        newRoute = Routes.objects.create(**body)
        serializer = RoutesSerializer(newRoute)
        return Response(serializer.data)
class adminRouteView(APIView):
    def get(self, request, pk):
        route = Routes.objects.get(id = pk)
        serializer = RoutesSerializer(route)
        return Response(serializer.data)
    def patch(self, request, pk):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        updateRoute = Routes.objects.get(id = pk)
        for key in body:
            setattr(updateRoute, key, body[key])
        updateRoute.save()
        serializer = RoutesSerializer(updateRoute)
        return Response(serializer.data)
    def delete(self, request, pk):
        deleteRoute = Routes.objects.get(id = pk).delete()
        return Response(deleteRoute[0])
class getroutes(APIView):
    def get(self,request,l1,l2):
        # location1=self.request.GET.get('l1')
        # location2=self.request.GET.get('l2')
        # location1='A'
        # location2='D'
        location1=l1
        location2=l2
        routes1 = Routes.objects.filter(fromStop = location1)
        routes2 =Routes.objects.filter(toStop=location2)
        v1={}
        v2={}
        q1=[]
        q2=[]
        v1[location1]=location1
        v2[location2]=location2

        for route in routes1:
            v1[route.toStop]=location1
            q1.append(route.toStop)
        for route in routes2:
            v2[route.fromStop]=location2
            q2.append(route.fromStop)
        itr=0
        threshold=10
        while itr<threshold:
            for stop in q1:
                if stop in v1:
                    continue
                routes=Routes.objects.filter(fromStop=stop)
                for route in routes:
                    if route.toStop not in v1:
                        v1[route.toStop]=stop
                        q1.append(route.toStop)
            for stop in q2:
                if stop in v2:
                    continue
                routes=Routes.objects.filter(toStop=stop)
                for route in routes:
                    if route.toStop not in v2:
                        v2[route.fromStop]=stop
                        q2.append(route.fromStop)
            itr+=1
            for stop in v1:
                if stop in v2:
                    path=[]
                    tmp=stop
                    while tmp!=v1[tmp]:
                        path.append(tmp)
                        tmp=v1[tmp]
                    path.append(tmp)
                    path.reverse()
                    path.pop()
                    print(path)
                    tmp=stop
                    print(tmp)
                    while tmp!=v2[tmp]:
                        print(tmp)
                        path.append(tmp)
                        tmp=v2[tmp]
                    path.append(tmp)
                    print(path)
                    serializer = PathSerializer(path)
                    return Response(path)
                    
                    
        return Response("hellp")
                    
                
            
                        
                
            
            



        

        

