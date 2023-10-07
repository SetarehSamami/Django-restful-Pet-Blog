from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer,UserUpdateSerializer
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser


User = get_user_model()

class UserRegister(APIView):
    def post(self,request): 
        ser_data=UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class Userview(APIView): 
    permission_classes = [IsAdminUser]

    def get(self,request):
        register=User.objects.all()
        ser_data=UserRegisterSerializer(instance=register, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)

class UserDelete(APIView):
    permission_classes = [IsAdminUser]

    def delete(self,request,pk):
        user=User.objects.get(pk=pk)
        user.delete()
        return Response({'message':'user deleted!'}, status=status.HTTP_200_OK)
    
class UserUpdate(APIView):
    permission_classes = [IsAdminUser]

    def put(self,request,pk):
        user=User.objects.get(pk=pk)
        ser_data = UserUpdateSerializer(instance=user, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


'''
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5Njc5MzU4NywiaWF0IjoxNjk2NzA3MTg3LCJqdGkiOiJkYWVlZDUwZWRhMDE0Yjg5OWRjMTQ2YjcxZmRmNGRjMiIsInVzZXJfaWQiOjR9.6ii9kylpQS9MrsuX6ueI2dRZrpVN5srD1OqivxvV2d4",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2NzA4OTg3LCJpYXQiOjE2OTY3MDcxODcsImp0aSI6ImU1ZWY4OTM1NGI3MzRjYjk4ODk0ZmVkZDY2MThiMWVkIiwidXNlcl9pZCI6NH0.nRbVrfMc_Jo8k08GFUO_CX1MA0aozTGLpqTTOsNwHSM"
}
   '''     