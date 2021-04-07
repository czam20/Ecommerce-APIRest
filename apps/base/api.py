from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
class GeneralViewSet(viewsets.ModelViewSet):
    serializer_class = None
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model 
        return model.objects.filter(state = True)


