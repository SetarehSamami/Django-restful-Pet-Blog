from rest_framework import serializers
from .models import User



class UserRegisterSerializer(serializers.ModelSerializer):
    password_comfirm = serializers.CharField(required= True, write_only= True)

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only":True},
        }
    
    
    def validate(self,data):
        if data["password"] != data["password_comfirm"]:
            raise serializers.ValidationError("passwords must match")
        return data
        
   
    def create(self, validated_data):
        del validated_data["password_comfirm"]
        del validated_data["is_active"]
        del validated_data["is_admin"]
        return User.objects.create_user(**validated_data)
   

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
