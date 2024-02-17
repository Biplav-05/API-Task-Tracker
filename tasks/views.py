from django.shortcuts import render
from rest_framework.views import APIView
from .models import Person
from rest_framework.response import Response
from .serializer import PersonSerializer

# Create your views here.
class PersonTestView(APIView):
    def get(self, request):
        person=Person.objects.all()
        if person:
            serializer=PersonSerializer(person, many=True)
            return Response(data=serializer.data)
        return Response(data=person)