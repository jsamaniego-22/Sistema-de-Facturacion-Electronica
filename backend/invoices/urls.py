# invoices/urls.py
from rest_framework.routers import DefaultRouter
from .views import ReceptorViewSet, EmisorViewSet, FacturaViewSet

router = DefaultRouter()
router.register(r'clientes', ReceptorViewSet)
router.register(r'emisores', EmisorViewSet)
router.register(r'facturas', FacturaViewSet)

urlpatterns = router.urls
