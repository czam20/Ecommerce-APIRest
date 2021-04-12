from datetime import datetime

from rest_framework import status, generics, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import User
from apps.users.serializers import EmailSerializer, UserModelSerializer, UserLoginSerializer,UserSingUpSerializer, AccountVerificationSerializer, ResetPasswordSerializer

class UserLoginAPIView(TokenObtainPairView):
    """User login API view"""
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
class UserSingUpAPIView(APIView):
    """User sing up API view"""
    permission_classes = (AllowAny,)
    serializer_class = UserSingUpSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({'user': UserModelSerializer(user).data}, status = status.HTTP_201_CREATED)
    
class AccountVerificationAPIView(APIView):
    """Account verfication API view"""
    serializer_class = AccountVerificationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'message':'¡Cuenta verificada!'}, status = status.HTTP_200_OK)
    
class ResetPasswordRequestTokenAPIView(APIView):
    """Provide a verification token that is sent by email to reset password"""
    serializer_class = EmailSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        return Response({'message':'Se ha enviado un enlace de restauracion al correo'}, status = status.HTTP_200_OK)
        
class ResetPasswordConfirmAPIView(APIView):
    serializer_class =  ResetPasswordSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'message':'¡Cambio de contraseña exitoso!'}, status = status.HTTP_200_OK)

"""class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response ({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Incio de sesión exitoso'
                        }, 
                        status = status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response ({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Incio de sesión exitoso'
                        }, 
                        status = status.HTTP_201_CREATED)
            else:
                return Response ({'error' : 'Este usuario no puede iniciar sesión'}, 
                                 status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response ({'error' : 'Nombre de usuario o contraseña incorrectos.'}, 
                             status = status.HTTP_400_BAD_REQUEST)
        return Response(status = status.HTTP_200_OK) 

class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = request.POST.get('token')
            token = Token.objects.filter(key = token).first()
            
            if token:
                user = token.user
                
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                            
                token.delete()
                
                return Response({'message':'Sesión finalizada'}, status = status.HTTP_200_OK)
            
            return Response({'error':'Debe iniciar sesión antes'}, status = status.HTTP_400_BAD_REQUEST)
                
        except:
            return  Response({'error':'No se ha encontado token en la petición'}, status = status.HTTP_409_CONFLICT)
        
    """
    
    