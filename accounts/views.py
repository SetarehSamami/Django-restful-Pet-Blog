from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer,UserUpdateSerializer
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser


User = get_user_model()

class UserRegister(APIView):
    '''
    Register User.
    '''
    
    serializer_class = UserRegisterSerializer
    def post(self,request): 
        ser_data=UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class Userview(APIView): 
    '''
    List of Users.
    '''

    permission_classes = [IsAdminUser]
    serializer_class = UserRegisterSerializer

    def get(self,request):
        register=User.objects.all()
        ser_data=UserRegisterSerializer(instance=register, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)

class UserDelete(APIView):
    '''
    Delete User.
    '''
    
    permission_classes = [IsAdminUser]
    serializer_class = UserRegisterSerializer
    
    def delete(self,request,pk):
        user=User.objects.get(pk=pk)
        user.delete()
        return Response({'message':'user deleted!'}, status=status.HTTP_200_OK)
    
class UserUpdate(APIView):
    '''
    Update User.
    '''
    
    permission_classes = [IsAdminUser]
    serializer_class = UserUpdateSerializer

    def put(self,request,pk):
        user=User.objects.get(pk=pk)
        ser_data = UserUpdateSerializer(instance=user, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

 