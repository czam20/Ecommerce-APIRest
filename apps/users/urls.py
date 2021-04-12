from django.urls import path
from apps.users.views import UserLoginAPIView, UserSingUpAPIView, AccountVerificationAPIView, ResetPasswordRequestTokenAPIView, ResetPasswordConfirmAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('singup/', UserSingUpAPIView.as_view(), name='singup'),
    path('verify/', AccountVerificationAPIView.as_view(), name='verify'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset-password/', ResetPasswordRequestTokenAPIView.as_view(), name='reset_password'),
    path('reset-password/confirm', ResetPasswordConfirmAPIView.as_view(), name='reset_password_confirm'),
]
