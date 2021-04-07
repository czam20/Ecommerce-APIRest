from apps.base.api import GeneralViewSet
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated

class MeasureUnitViewSet(GeneralViewSet):
    serializer_class = MeasureUnitSerializer

class IndicatorViewSet(GeneralViewSet):
    serializer_class = IndicatorSerializer
    
class CategoryProductViewSet(GeneralViewSet):
    serializer_class = CategoryProductSerializer