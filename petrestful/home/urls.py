from django.urls import path
from . import views


urlpatterns = [
    path('post/',views.PostListView.as_view()),
    path('create-post/',views.PostCreateView.as_view()),
    path('delete/<int:pk>', views.PostDeleteView.as_view()),
    path('update/<int:pk>', views.PostUpdateView.as_view()),
    path('Category/',views.CategoryListView.as_view()),
    path('create-Category/',views.CategoryCreateView.as_view()),
    path('delete/<int:pk>', views.CategoryDeleteView.as_view()),
    path('update/<int:pk>', views.CategoryUpdateView.as_view()),
    path('Comment/',views.CommentListView.as_view()),
    path('create-Comment/',views.CommentCreateView.as_view()),
    path('delete/<int:pk>', views.CommentDeleteView.as_view()),
    path('update/<int:pk>', views.CommentUpdateView.as_view()),
    path('Answer/',views.AnswerListView.as_view()),
    path('create-Answer/',views.AnswerCreateView.as_view()),
    path('delete/<int:pk>', views.AnswerDeleteView.as_view()),
    path('update/<int:pk>', views.AnswerUpdateView.as_view()),

]
