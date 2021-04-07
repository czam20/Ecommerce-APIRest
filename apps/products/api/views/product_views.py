from django.http import response

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from apps.products.api.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """Product view set"""
    serializer_class = ProductSerializer
    lookup_field = 'name'
    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
        
    def get_permissions(self):
        """Asing permissions based on actions"""
        if self.action in ['list', 'retrieve']:
            permissions = [AllowAny]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated, IsAdminUser]
        
        return [permission() for permission in permissions]
        
    def create(self, request):
        #send information to the db
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Producto creado'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response(status = status.HTTP_200_OK)
        return Response({'error':'No existe un producto con esas caracteristicas'}, status = status.HTTP_400_BAD_REQUEST)
    
    
    
"""#Vistas genéricas
class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True)
   
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Producto creado'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def patch(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = self.serializer_class(product)
            return Response(product_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':'No existe un producto con esas caracteristicas'}, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response(status = status.HTTP_200_OK)
        return Response({'error':'No existe un producto con esas caracteristicas'}, status = status.HTTP_400_BAD_REQUEST)
    """
    







