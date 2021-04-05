from django.db import models
from django.db.models.deletion import CASCADE
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class MeasureUnit(BaseModel):
    """Model definition for ."""

    # TODO: Define fields here
    description = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for ."""

        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'

    def __str__(self):
        """Unicode representation of ."""
        return self.description
    
class CategoryProduct(BaseModel):
    
    description = models.CharField('Descricion', max_length=50, unique=True, null=False, blank=False)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Categoria de producto'
        verbose_name_plural = 'Categorias de Productos'

    def __str__(self):
        return self.description
    
class Indicator(BaseModel):
    
    descount_value = models.PositiveSmallIntegerField(default = 0)
    category_produt = models.ForeignKey(CategoryProduct, on_delete=CASCADE, verbose_name="Indicador de Oferta")
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):
        return f'Oferta de la categoria{self.category_produt} : {self.descount_value}%'

class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField('Nombre de Producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripción del Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/',blank = True, null=True)
    
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=CASCADE, verbose_name='Unidad de medida', null = True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=CASCADE, verbose_name='Categoria del producto', null = True)
    
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation for Product."""
        return self.name


