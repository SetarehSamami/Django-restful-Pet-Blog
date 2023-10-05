from django.urls import path
from . import views


urlpatterns = [
    path('post/',views.PostListView.as_view()),
    path('create-post/',views.PostCreateView.as_view()),
    path('delete-post/<int:pk>', views.PostDeleteView.as_view()),
    path('update-post/<int:pk>', views.PostUpdateView.as_view()),
    path('category/',views.CategoryListView.as_view()),
    path('create-category/',views.CategoryCreateView.as_view()),
    path('delete-category/<int:pk>', views.CategoryDeleteView.as_view()),
    path('update-category/<int:pk>', views.CategoryUpdateView.as_view()),
    path('comment/',views.CommentListView.as_view()),
    path('create-comment/',views.CommentCreateView.as_view()),
    path('delete-comment/<int:pk>', views.CommentDeleteView.as_view()),
    path('update-comment/<int:pk>', views.CommentUpdateView.as_view()),
    path('answer/',views.AnswerListView.as_view()),
    path('create-answer/',views.AnswerCreateView.as_view()),
    path('delete-answer/<int:pk>', views.AnswerDeleteView.as_view()),
    path('update-answer/<int:pk>', views.AnswerUpdateView.as_view()),

]
