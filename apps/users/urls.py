from django.urls import path
#from apps.users.api import UserAPIView
from apps.users.views import UserLoginAPIView, UserSingUpAPIView, AccountVerificationAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('singup/', UserSingUpAPIView.as_view(), name='singup'),
    path('verify/', AccountVerificationAPIView.as_view(), name='verify'),
]
