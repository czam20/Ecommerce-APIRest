# Generated by Django 3.1.7 on 2021-03-30 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_data', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_data', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descricion')),
            ],
            options={
                'verbose_name': 'Categoria de producto',
                'verbose_name_plural': 'Categorias de Productos',
            },
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_data', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_data', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descrition')),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidades de Medidas',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_data', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_data', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre de Producto')),
                ('description', models.TextField(verbose_name='Descripción del Producto')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen del Producto')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_data', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_data', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
                ('category_produt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Indicador de Oferta')),
            ],
            options={
                'verbose_name': 'Indicador de Oferta',
                'verbose_name_plural': 'Indicadores de Ofertas',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_data', models.DateField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_data', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminación')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Nombre de Producto')),
                ('description', models.TextField(verbose_name='Descripción del Producto')),
                ('image', models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagen del Producto')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMeasureUnit',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_data', models.DateField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_data', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminación')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descrition')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Unidad de Medida',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIndicator',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_data', models.DateField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_data', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminación')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_produt', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Indicador de Oferta')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Indicador de Oferta',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategoryProduct',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_data', models.DateField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_data', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminación')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descricion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('measure_unit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Unidad de medida')),
            ],
            options={
                'verbose_name': 'historical Categoria de producto',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='measure_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de medida'),
        ),
    ]