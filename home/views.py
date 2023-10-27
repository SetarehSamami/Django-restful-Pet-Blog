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
    '''
    List of Posts.
    '''

    pagination_class= PageNumberPagination
    serializer_class = PostSerializer

    def get(self,request):
        post=Post.objects.all()
        paginator = self.pagination_class()
        result_page=paginator.paginate_queryset(post,request)
        ser_data=PostSerializer(instance=result_page , many=True)
        return Response(data=ser_data.data)

class PostCreateView(APIView):   
    '''
    Create a new Post.
    '''

    permission_classes=[IsAuthenticated,] 
    serializer_class = PostSerializer

    def post(self,request):
        ser_data=PostSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class PostUpdateView(APIView):
    '''
    Update Post.
    '''

    permission_classes=[IsOwnerOrReadOnly,] 
    serializer_class = PostSerializer
    
    def put(self,request,pk):
        post=Post.objects.get(pk=pk)
        self.check_object_permissions(request,post)
        ser_data=PostSerializer(instance=post, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class PostDeleteView(APIView): 
    '''
    Delete Post.
    '''
    
    permission_classes=[IsOwnerOrReadOnly,] 
    serializer_class = PostSerializer
   
    def delete(self,request,pk):
        post=Post.objects.get(pk=pk)
        self.check_object_permissions(request,post)
        post.delete()
        return Response({'message':'post deleted!'}, status=status.HTTP_200_OK)

class CategoryListView(APIView):
    '''
    List of Categories.
    '''


    pagination_class= PageNumberPagination
    serializer_class = CategorySerializer

    def get(self,request):
        category=Category.objects.all()
        paginator = self.pagination_class()
        result_page=paginator.paginate_queryset(category,request)
        ser_data=CategorySerializer(instance=result_page , many=True)
        return Response(data=ser_data.data)
    
class CategoryCreateView(APIView): 
    '''
    Create a new Category.
    '''

    permission_classes=[IsAdminUser,]
    serializer_class = CategorySerializer 

    def post(self,request):
        ser_data=CategorySerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CategoryUpdateView(APIView): 
    '''
    Update Category.
    '''

    permission_classes=[IsAdminUser,] 
    serializer_class = CategorySerializer

    def put(self,request,pk):
        category=Category.objects.get(pk=pk)
        ser_data=CategorySerializer(instance=category, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CategoryDeleteView(APIView):
    '''
    Delete Category.
    '''
    
    permission_classes=[IsAdminUser,] 
    serializer_class = CategorySerializer

    def delete(self,request,pk):
        category=Category.objects.get(pk=pk)
        category.delete()
        return Response({'message':'Category deleted!'}, status=status.HTTP_200_OK)

class CommentListView(APIView):
    '''
    List of Comments.
    '''

    pagination_class= PageNumberPagination
    serializer_class = CommentSerializer


    def get(self,request):
        comment=Comment.objects.all()
        paginator = self.pagination_class()
        result_page=paginator.paginate_queryset(comment,request)
        ser_data=CommentSerializer(instance=result_page , many=True)
        return Response(data=ser_data.data)

class CommentCreateView(APIView):  
    '''
    Create a new Comment.
    '''

    permission_classes=[IsAuthenticated,] 
    serializer_class = CommentSerializer
  
    def post(self,request):
        ser_data=CommentSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentUpdateView(APIView):
    '''
    Update Comment.
    '''

    permission_classes=[IsOwnerOrReadOnly,] 
    serializer_class = CommentSerializer
    
    def put(self,request,pk):
        comment=Comment.objects.get(pk=pk)
        self.check_object_permissions(request,comment)
        ser_data=CommentSerializer(instance=comment, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentDeleteView(APIView):  
    '''
    Delete Comment.
    '''
    
    permission_classes=[IsOwnerOrReadOnly,] 
    serializer_class = CommentSerializer
      
    def delete(self,request,pk):
        comment=Comment.objects.get(pk=pk)
        self.check_object_permissions(request,comment)
        comment.delete()
        return Response({'message':'Comment deleted!'}, status=status.HTTP_200_OK)
        
class AnswerListView(APIView):
    '''
    List of Answers.
    '''

    pagination_class= PageNumberPagination
    serializer_class = AnswerSerializer

    def get(self,request):
        answer=Answer.objects.all()
        paginator = self.pagination_class()
        result_page=paginator.paginate_queryset(answer,request)
        ser_data=AnswerSerializer(instance=result_page , many=True)
        return Response(data=ser_data.data)

class AnswerCreateView(APIView):
    '''
    Create a new Answer.
    '''
    
    permission_classes=[IsAuthenticated,] 
    serializer_class = AnswerSerializer

    def post(self,request):
        ser_data=AnswerSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class AnswerUpdateView(APIView):   
    '''
    Update Comment's Answer.
    '''
 
    permission_classes=[IsOwnerOrReadOnly,] 
    serializer_class = AnswerSerializer

    def put(self,request,pk):
        answer=Answer.objects.get(pk=pk)
        self.check_object_permissions(request,answer)
        ser_data=AnswerSerializer(instance=answer, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class AnswerDeleteView(APIView):  
    '''
    Delete Comment's Answer.
    '''
     
    permission_classes=[IsOwnerOrReadOnly,] 
    serializer_class = AnswerSerializer
     
    def delete(self,request,pk):
        answer=Answer.objects.get(pk=pk)
        self.check_object_permissions(request,answer)
        answer.delete()
        return Response({'message':'Answer deleted!'}, status=status.HTTP_200_OK)
        
        