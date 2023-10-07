from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework.pagination import PageNumberPagination
from permissions import IsOwnerOrReadOnly
from .models import Post, Category, Comment, Answer
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, AnswerSerializer


class PostListView(APIView):
    pagination_class= PageNumberPagination

    def get(self,request):
        post=Post.objects.all()
        paginator = self.pagination_class()
        result_page=paginator.paginate_queryset(post,request)
        ser_data=PostSerializer(instance=result_page , many=True)
        return Response(data=ser_data.data)

class PostCreateView(APIView):   
    permission_classes=[IsAuthenticated,] 

    def post(self,request):
        ser_data=PostSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class PostUpdateView(APIView):
    permission_classes=[IsOwnerOrReadOnly,] 
    
    def put(self,request,pk):
        post=Post.objects.get(pk=pk)
        self.check_object_permissions(request,post)
        ser_data=PostSerializer(instance=post, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class PostDeleteView(APIView):     
    permission_classes=[IsOwnerOrReadOnly,] 
   
    def delete(self,request,pk):
        post=Post.objects.get(pk=pk)
        self.check_object_permissions(request,post)
        post.delete()
        return Response({'message':'post deleted!'}, status=status.HTTP_200_OK)

class CategoryListView(APIView):
    pagination_class= PageNumberPagination

    def get(self,request):
        category=Category.objects.all()
        paginator = self.pagination_class()
        result_page=paginator.paginate_queryset(category,request)
        ser_data=CategorySerializer(instance=result_page , many=True)
        return Response(data=ser_data.data)
    
class CategoryCreateView(APIView): 
    permission_classes=[IsAdminUser,] 

    def post(self,request):
        ser_data=CategorySerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CategoryUpdateView(APIView): 
    permission_classes=[IsAdminUser,] 

    def put(self,request,pk):
        category=Category.objects.get(pk=pk)
        ser_data=CategorySerializer(instance=category, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CategoryDeleteView(APIView):
    permission_classes=[IsAdminUser,] 

    def delete(self,request,pk):
        category=Category.objects.get(pk=pk)
        category.delete()
        return Response({'message':'Category deleted!'}, status=status.HTTP_200_OK)

class CommentListView(APIView):
    pagination_class= PageNumberPagination

    def get(self,request):
        comment=Comment.objects.all()
        paginator = self.pagination_class()
        result_page=paginator.paginate_queryset(comment,request)
        ser_data=CommentSerializer(instance=result_page , many=True)
        return Response(data=ser_data.data)

class CommentCreateView(APIView):  
    permission_classes=[IsAuthenticated,] 
  
    def post(self,request):
        ser_data=CommentSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentUpdateView(APIView):
    permission_classes=[IsOwnerOrReadOnly,] 
    
    def put(self,request,pk):
        comment=Comment.objects.get(pk=pk)
        self.check_object_permissions(request,comment)
        ser_data=CommentSerializer(instance=comment, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentDeleteView(APIView):  
    permission_classes=[IsOwnerOrReadOnly,] 
      
    def delete(self,request,pk):
        comment=Comment.objects.get(pk=pk)
        self.check_object_permissions(request,comment)
        comment.delete()
        return Response({'message':'Comment deleted!'}, status=status.HTTP_200_OK)
        
class AnswerListView(APIView):
    pagination_class= PageNumberPagination

    def get(self,request):
        answer=Answer.objects.all()
        paginator = self.pagination_class()
        result_page=paginator.paginate_queryset(answer,request)
        ser_data=AnswerSerializer(instance=result_page , many=True)
        return Response(data=ser_data.data)

class AnswerCreateView(APIView):    
    permission_classes=[IsAuthenticated,] 

    def post(self,request):
        ser_data=AnswerSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class AnswerUpdateView(APIView):    
    permission_classes=[IsOwnerOrReadOnly,] 

    def put(self,request,pk):
        answer=Answer.objects.get(pk=pk)
        self.check_object_permissions(request,answer)
        ser_data=AnswerSerializer(instance=answer, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class AnswerDeleteView(APIView):   
    permission_classes=[IsOwnerOrReadOnly,] 
     
    def delete(self,request,pk):
        answer=Answer.objects.get(pk=pk)
        self.check_object_permissions(request,answer)
        answer.delete()
        return Response({'message':'Answer deleted!'}, status=status.HTTP_200_OK)
        
        