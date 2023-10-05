from rest_framework import serializers
from .models import Post, Category, Answer, Comment



class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = "__all__"

