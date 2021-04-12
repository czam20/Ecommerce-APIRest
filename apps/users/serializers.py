from django.conf import settings
from django.contrib.auth import models, authenticate, password_validation
from django.db.models import query
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from datetime import timedelta
import jwt
from apps.users.models import User
class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""
    class Meta:
        model = User
        fields = ('name', 'last_name', 'username', 'password', 'email')

class UserLoginSerializer(TokenObtainPairSerializer):
    """User login serializer"""
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)
    
    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Credenciales invalidas')
        if not user.is_verified:
            raise serializers.ValidationError('Cuenta no ativa :(')
        self.context['user'] = user
        return data
class UserSingUpSerializer(serializers.Serializer):
    """User sing up serializer"""
    name = serializers.CharField(max_length=250)
    last_name = serializers.CharField(max_length=250)
    username = serializers.CharField(min_length=5,
                                    max_length=20,
                                    validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, max_length=20)
    password_confirmation = serializers.CharField(min_length=8, max_length=20)
    
    
    def validate(self, data):
        """verify password match"""
        password = data['password']
        password_conf = data['password_confirmation']
        if password != password_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(password)
        return data
    
    def create(self, data):
        """Handle user creation"""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False)
        self.send_confirmation_email(user)
        return user
    
    def send_confirmation_email(self, user):
        """Send account vefirication link to given user."""
        verification_token = self.gen_verification_token(user)
        subject = "¡Bienvenido @{}! Verifica tu cuenta para empezar a disfrutar de mi super App".format(user.username)
        from_email = 'Comparte ride <cczam@gmail.com>'
        content = render_to_string('emails/users/account_verification.html', 
        {'token': verification_token, 'user': user})
        html_content = '<p>This is an <strong>important</strong> message.</p>'
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()
        
    def gen_verification_token(self, user):
        """Create JWT token that usar can use to verificate account."""
        exp_date = timezone.now() + timedelta(days=3)
        payload = {
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }
        
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        
        return token
         
class UserListSerializer(serializers.ModelSerializer):
    """User list serializer"""
    class Meta:
        model = User
            
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'name': instance['name'],
            'last_name': instance['last_name'],
            'email': instance['email'],
            'username': instance['username'],
            'password': instance['password']
         }
        

class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer""" 
    token = serializers.CharField()
    
    def validate_token(self, data):
        """Verify token is valid"""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms = ["HS256"])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('El enlace de verificación ha expirado')
        except jwt.PyJWTError:
            raise serializers.ValidationErrors('Token inválido')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Token inválido')
        
        self.context['payload']= payload
        return data
    
    def save(self):
        """Update user's verified status"""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()  
class EmailSerializer(serializers.Serializer):
    """Email serializer"""
    email = serializers.EmailField()
    
    def validate(self, data):
        """Verify user alredy exist"""
        email = data['email']
        try:
            user = User.objects.get(email = email)
            self.send_email(user=user)
        except:
            raise serializers.ValidationError({
                'email': "No se encontró un usuario asociado a este email. Intente con otro email.",
            }) 
            
        return data
    
    def send_email(self, user):
        """Send account vefirication link to given user."""
        verification_token = self.gen_verification_token(user)
        subject = "¡Hola @{}! ¿Has solicitado cambiar tu contraseña?".format(user.username)
        from_email = 'Comparte ride <cczam@gmail.com>'
        content = render_to_string('emails/users/account_verification.html', 
        {'token': verification_token, 'user': user})
        html_content = '<p>This is an <strong>important</strong> message.</p>'
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()
        
    def gen_verification_token(self, user):
        """Create JWT token that usar can use to verificate account."""
        exp_date = timezone.now() + timedelta(days=1)
        payload = {
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'email_reset_password'
        }
        
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        
        return token 
class ResetPasswordSerializer(serializers.Serializer):
    """Reset password serializer"""
    token = serializers.CharField()
    new_password = serializers.CharField()
    password_confirmation = serializers.CharField()
    
    def validate_token(self, data):
        """Verify token is valid"""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms = ["HS256"])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('El enlace de verificación ha expirado')
        except jwt.PyJWTError:
            raise serializers.ValidationErrors('Token inválido')
        if payload['type'] != 'email_reset_password':
            raise serializers.ValidationError('Token inválido')
        
        self.context['payload']= payload
        return data
    
    def validate(self, data):
        """Verify passwords match"""
        password = data['new_password']
        password_conf = data['password_confirmation']
        if password != password_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(password)
        return data
    
    def save(self):
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.set_password(self.validated_data['new_password'])
        user.save()        
        
    