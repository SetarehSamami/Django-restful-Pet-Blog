from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Category, Comment, Answer
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, AnswerSerializer


class PostListView(APIView):
    def View(self,request):
        post=Post.objects.all()
        ser_data=PostSerializer(instance=post , many=True)
        return Response(data=ser_data.data)

class PostCreateView(APIView):    
    def Create(self,request):
        ser_data=PostSerializer(data=request.POST)
        if ser_data.ia_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class PostUpdateView(APIView):    
    def Update(self,request,pk):
        post=Post.object.get(pk=pk)
        ser_data=PostSerializer(instance=post, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class PostDeleteView(APIView):        
    def Delete(self,request,pk):
        post=Post.object.get(pk=pk)
        post.delete()
        return Response({'message':'post deleted!'}, status=status.HTTP_200_OK)

class CategoryListView(APIView):
    def View(self,request):
        category=Category.objects.all()
        ser_data=CategorySerializer(instance=category , many=True)
        return Response(data=ser_data.data)
    
class CategoryCreateView(APIView): 
    def Create(self,request):
        ser_data=CategorySerializer(data=request.POST)
        if ser_data.ia_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CategoryUpdateView(APIView):    
    def Update(self,request,pk):
        category=Category.object.get(pk=pk)
        ser_data=CategorySerializer(instance=category, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CategoryDeleteView(APIView):
    def Delete(self,request,pk):
        category=Category.object.get(pk=pk)
        category.delete()
        return Response({'message':'Category deleted!'}, status=status.HTTP_200_OK)


class CommentListView(APIView):
    def View(self,request):
        comment=Comment.objects.all()
        ser_data=CommentSerializer(instance=comment , many=True)
        return Response(data=ser_data.data)

class CommentCreateView(APIView):    
    def Create(self,request):
        ser_data=CommentSerializer(data=request.POST)
        if ser_data.ia_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentUpdateView(APIView):    
    def Update(self,request,pk):
        comment=Comment.object.get(pk=pk)
        ser_data=CommentSerializer(instance=comment, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentDeleteView(APIView):        
    def Delete(self,request,pk):
        post=Post.object.get(pk=pk)
        post.delete()
        return Response({'message':'Comment deleted!'}, status=status.HTTP_200_OK)
        

class AnswerListView(APIView):
    def View(self,request):
        answer=Answer.objects.all()
        ser_data=AnswerSerializer(instance=answer , many=True)
        return Response(data=ser_data.data)

class AnswerCreateView(APIView):    
    def Create(self,request):
        ser_data=AnswerSerializer(data=request.POST)
        if ser_data.ia_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class AnswerUpdateView(APIView):    
    def Update(self,request,pk):
        answer=Answer.object.get(pk=pk)
        ser_data=AnswerSerializer(instance=answer, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class AnswerDeleteView(APIView):        
    def Delete(self,request,pk):
        post=Post.object.get(pk=pk)
        post.delete()
        return Response({'message':'Answer deleted!'}, status=status.HTTP_200_OK)
        
        