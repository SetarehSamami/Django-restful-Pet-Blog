from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer
from rest_framework import status



class UserRegister(APIView):
    serializer_class = UserRegisterSerializer
    
    def post(self,request):
        ser_data=UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            User.objects.create_user(
                username=ser_data.validated_data['username'],
                password=ser_data.validated_data['password'],
                email=ser_data.validated_data['email'],
                age=ser_data.validated_data['age']
            )
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors , status=status.HTTP_400_BAD_REQUEST)
    

