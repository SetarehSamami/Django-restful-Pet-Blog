from rest_framework import serializers





class PersonSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	username = serializers.CharField()
	age = serializers.IntegerField()
	email = serializers.EmailField()

