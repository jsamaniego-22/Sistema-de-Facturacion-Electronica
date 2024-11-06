from django.db import models 

# Modelo de Factura (Datos Generales)
class Factura(models.Model):
    numero_factura = models.CharField(max_length=20, primary_key=True)  # Clave primaria
    ruc_receptor = models.CharField(max_length=20)  # Relación con el receptor por RUC
    fecha_factura = models.DateField()  # Fecha de la factura

    iAmb = models.CharField(max_length=10)  # Ambiente de emisión
    iTpEmis = models.CharField(max_length=10)  # Tipo de emisión
    iDoc = models.CharField(max_length=10)  # Tipo de documento
    dNroDF = models.CharField(max_length=20)  # Número de documento fiscal
    dPtoFacDF = models.CharField(max_length=10)  # Punto de facturación
    dSeg = models.CharField(max_length=20)  # Número de seguridad
    dFechaEm = models.DateField()  # Fecha de emisión
    dFechaSalida = models.DateField(blank=True, null=True)  # Fecha de salida
    iNatOp = models.CharField(max_length=10)  # Naturaleza de la operación
    iTipoOp = models.CharField(max_length=10)  # Tipo de operación
    iDest = models.CharField(max_length=10)  # Destino
    iFormCAFE = models.CharField(max_length=10)  # Formato del comprobante
    iEntCAFE = models.CharField(max_length=10)  # Entidad del comprobante
    dEnvFE = models.CharField(max_length=20)  # Número de envío de la FE
    iProGen = models.CharField(max_length=10)  # Proceso general
    iTipoTranVenta = models.CharField(max_length=10)  # Tipo de transacción de venta

    def __str__(self):
        return f"Factura {self.numero_factura}"

# Modelo de Emisor
class Emisor(models.Model):
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE, related_name="emisor")

    dTipoRuc = models.CharField(max_length=10)  # Tipo de RUC
    dRuc = models.CharField(max_length=20)  # RUC del emisor
    dDV = models.CharField(max_length=5)  # Dígito verificador del emisor
    dNombEm = models.CharField(max_length=100)  # Nombre del emisor
    dSucEm = models.CharField(max_length=10)  # Código de sucursal del emisor
    dCoordEm = models.CharField(max_length=50)  # Coordenadas de ubicación del emisor
    dDirecEm = models.CharField(max_length=255)  # Dirección del emisor
    dCodUbi = models.CharField(max_length=10)  # Código de ubicación
    dCorreg = models.CharField(max_length=50)  # Corregimiento
    dDistr = models.CharField(max_length=50)  # Distrito
    dProv = models.CharField(max_length=50)  # Provincia
    dTfnEm = models.CharField(max_length=15)  # Teléfono del emisor

    def __str__(self):
        return f"Emisor {self.dNombEm} - {self.dRuc}"

# Modelo de Receptor
class Receptor(models.Model):
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE, related_name="receptor")

    iTipoRec = models.CharField(max_length=10)  # Tipo de receptor
    dTipoRuc = models.CharField(max_length=10)  # Tipo de RUC del receptor
    dRuc = models.CharField(max_length=20)  # RUC del receptor
    dNombRec = models.CharField(max_length=100)  # Nombre del receptor
    cPaisRec = models.CharField(max_length=3)  # Código de país del receptor

    def __str__(self):
        return f"Receptor {self.dNombRec} - {self.dRuc}"

# Modelo de Detalle de Items
class ItemDetalle(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="items")

    dSecItem = models.IntegerField()  # Número de secuencia del ítem
    dDescProd = models.CharField(max_length=255)  # Descripción del producto o servicio
    dCodProd = models.CharField(max_length=50)  # Código del producto
    dCantCodInt = models.DecimalField(max_digits=10, decimal_places=2)  # Cantidad del ítem
    dCodCPBScmp = models.CharField(max_length=50)  # Código del ítem según el catálogo
    dPrUnit = models.DecimalField(max_digits=10, decimal_places=2)  # Precio unitario
    dPrUnitDesc = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Descuento aplicado
    dPrItem = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del ítem
    dPrAcarItem = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Accesorio del precio
    dPrSegItem = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Precio secundario
    dValTotItem = models.DecimalField(max_digits=10, decimal_places=2)  # Valor total
    dTasaITBMS = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Tasa de ITBMS
    dValITBMS = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Valor del ITBMS

    def __str__(self):
        return f"Item {self.dDescProd} - Cantidad {self.dCantCodInt}"

# Modelo de Totales de la Factura
class TotalesFactura(models.Model):
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE, related_name="totales")

    dTotNeto = models.DecimalField(max_digits=10, decimal_places=2)  # Total neto
    dTotITBMS = models.DecimalField(max_digits=10, decimal_places=2)  # Total ITBMS
    dTotGravado = models.DecimalField(max_digits=10, decimal_places=2)  # Total gravado
    dTotDesc = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Total de descuentos
    dVTot = models.DecimalField(max_digits=10, decimal_places=2)  # Valor total de la factura
    dTotRec = models.DecimalField(max_digits=10, decimal_places=2)  # Total recibido
    iPzPag = models.CharField(max_length=20)  # Plazo de pago
    dNroItems = models.IntegerField()  # Número de ítems
    dVTotItems = models.DecimalField(max_digits=10, decimal_places=2)  # Valor total de los ítems
    iFormaPago = models.CharField(max_length=20)  # Código de forma de pago
    dVlrCuota = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Valor de la cuota

    def __str__(self):
        return f"Totales de Factura {self.factura.numero_factura}"

# Modelo de Pedido Comercial Global
class PedidoComercial(models.Model):
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE, related_name="pedido_comercial")

    dNroPed = models.CharField(max_length=20)  # Número de pedido
    dCodSisEm = models.CharField(max_length=20)  # Código del sistema del emisor
    dInfEmPedGl = models.TextField(blank=True, null=True)  # Información adicional del pedido

    def __str__(self):
        return f"Pedido Comercial {self.dNroPed}"

# Modelo de Firma Digital
class FirmaDigital(models.Model):
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE, related_name="firma_digital")

    CanonicalizationMethod = models.CharField(max_length=100)
    SignatureMethod = models.CharField(max_length=100)
    Transforms = models.CharField(max_length=100)
    DigestMethod = models.CharField(max_length=100)
    DigestValue = models.CharField(max_length=255)
    SignatureValue = models.TextField()
    X509SubjectName = models.TextField()
    X509Certificate = models.TextField()

    def __str__(self):
        return f"Firma Digital para Factura {self.factura.numero_factura}"

# Modelo de QR de Factura
class QRFactura(models.Model):
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE, related_name="qr_factura")

    dQRCode = models.ImageField(upload_to="qr_codes/")  # Imagen del código QR generado

    def __str__(self):
        return f"QR para Factura {self.factura.numero_factura}"
