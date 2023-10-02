from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer


class Home(APIView):
    def get(self,request):
        person=Person.objects.all()
        s_data=PersonSerializer(instance=person , many=True)
        return Response(data=s_data.data)
    