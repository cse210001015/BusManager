from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serialisers import NoteSerializer


@api_view(['GET'])
def getRoutes(request):
    routes=[{'Endpoint':'/notes','method':'GET','body':None,'description':'Returns an array of notes'}]
    return Response(routes)
@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all()
    serialiser=NoteSerializer(notes,many=True)
    return Response(serialiser.data)
@api_view(['GET'])
def getNote(requset,pk):
    notes=Note.objects.get(id=pk)
    serialiser=NoteSerializer(notes)
    return Response(serialiser.data)

# Create your views here.
