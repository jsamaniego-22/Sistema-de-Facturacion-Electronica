# invoices/views.py
from rest_framework import viewsets
from .models import Receptor, Emisor, Factura
from .serializers import ReceptorSerializer, EmisorSerializer, FacturaSerializer

# Vista para listar y obtener los clientes (Receptor)
class ReceptorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Receptor.objects.all()
    serializer_class = ReceptorSerializer

# Vista para listar y obtener los emisores
class EmisorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Emisor.objects.all()
    serializer_class = EmisorSerializer

# Vista para listar y obtener facturas con sus detalles
class FacturaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
