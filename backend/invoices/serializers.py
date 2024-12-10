# invoices/serializers.py
from rest_framework import serializers
from .models import Receptor, Emisor, Factura, ItemDetalle, TotalesFactura

class ReceptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptor
        fields = '__all__'

class EmisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emisor
        fields = '__all__'

class ItemDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetalle
        fields = '__all__'

class TotalesFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalesFactura
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    emisor = EmisorSerializer(read_only=True)  # Relación OneToOne con Emisor
    receptor = ReceptorSerializer(read_only=True)  # Relación OneToOne con Receptor
    items = ItemDetalleSerializer(many=True, read_only=True)  # Relación ForeignKey con ItemDetalle
    totales = TotalesFacturaSerializer(read_only=True)  # Relación OneToOne con TotalesFactura

    class Meta:
        model = Factura
        fields = '__all__'
