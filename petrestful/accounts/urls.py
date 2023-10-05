from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('users/',views.Userview.as_view()),
    path('delete/<int:pk>', views.UserDelete.as_view()),
    path('update/<int:pk>', views.UserUpdate.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
'''
{
"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NjYwNzQzMiwiaWF0IjoxNjk2NTIxMDMyLCJqdGkiOiJjZDhmMjAwZDA3OWM0ZWY1YTgzNjg2ZTQ1ZTUwYzQxMSIsInVzZXJfaWQiOjN9.-Nf59XDijAVuyH9bLUF5cuk3_PCFvFR-obNtDepIhB4",
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2NTIxMzMyLCJpYXQiOjE2OTY1MjEwMzIsImp0aSI6IjM3Y2NjMTBhNWI0MzRlYTNhNDA0ZDUwNjExYjUxMjk1IiwidXNlcl9pZCI6M30.4LIx65zfTDWrD4VsP0pgee65vY9hI80F2qDqV2ObHSg"
}'''