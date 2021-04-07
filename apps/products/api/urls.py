from django.urls import path
from rest_framework import routers
from apps.products.api.views.product_views import ProductViewSet
from apps.products.api.views.general_views import CategoryProductViewSet, MeasureUnitViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename = 'products')
router.register(r'category-product', CategoryProductViewSet, basename = 'category_product')
router.register(r'measure-unit', MeasureUnitViewSet, basename = 'measure_unit')

urlpatterns = router.urls