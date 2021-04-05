from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.serializers import UserSerializer, UserListSerializer

@api_view(['GET', 'POST'])
def user_api_view(request): 
    #List
    if request.method == 'GET':
        #query
        users = User.objects.all().values('id', 'name', 'last_name', 'email', 'username','password')
        users_serializer = UserListSerializer(users, many = True) #many es para indicar si se envia uno o varios usuarios                     
        return Response(users_serializer.data, status = status.HTTP_200_OK)
    
    #Create
    elif request.method == 'POST':
        users_serializer = UserSerializer(data = request.data)
        #validation
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({'message':'Usuario creado'}, status = status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk=None):
    #Queryset
    user = User.objects.filter(id = pk).first()
    
    #Validation
    if user:
        #Retrieve
        if request.method == 'GET':
            user_serializer =  UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        
        #Update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #Delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario eliminado'}, status = status.HTTP_200_OK)
    
    return Response({'message':'Usuario no registrado'}, status = status.HTTP_400_BAD_REQUEST)