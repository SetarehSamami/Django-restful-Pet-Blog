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
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2NTMyODQzLCJpYXQiOjE2OTY1MjEwMzIsImp0aSI6IjA0MDg3Mzk2ZWE0MDRjM2Y5MmJkM2VjYjZmMTMzNDNkIiwidXNlcl9pZCI6M30.zV5Tq9EF6kllBx1h6Q0mLyqa2NXL5ouesz6w3vdNSvs"
}'''


'''
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NjYxOTE0NSwiaWF0IjoxNjk2NTMyNzQ1LCJqdGkiOiJkN2VlMDdmMGFkZmY0OTgxODk2OTE3NGE3NDI1MDg3NiIsInVzZXJfaWQiOjF9.m77nw3nf8rPV2l4JHw6NhN9b7mlXMbC07a1TfSTUFgU",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2NTMzNzAwLCJpYXQiOjE2OTY1MzI3NDUsImp0aSI6IjlkNDFlNjI4MTFmNzRiNTk4ZjFhMjQ0NDkzNGJlYTUxIiwidXNlcl9pZCI6MX0.FTSOuHimdGHadKHBwG7n_-Lm04mhjNq1SSOr7KYpnm4"
}'''
'''
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NjYxOTk1MCwiaWF0IjoxNjk2NTMzNTUwLCJqdGkiOiIyNjQ1ZjEyY2JiOTM0N2FkYTZhMTgxNTRjM2NjZTg5MSIsInVzZXJfaWQiOjJ9.nSHDOPfsrOzSU3b0ZZt7tYn88KMonfR1ASTrQLRgzBA",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2NTMzODUwLCJpYXQiOjE2OTY1MzM1NTAsImp0aSI6IjA5OGY1MTg5NDcxYzRmNzU5ZDAzMWY5NTA2ZTM4YjQ2IiwidXNlcl9pZCI6Mn0._Kst9Cs1kyD7OBjNnk3DZmYH5lkx0miGoK5yOaNCFM4"
}'''