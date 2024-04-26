# Generated by Django 5.0.2 on 2024-02-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='Stock Keeping Unit'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_count',
            field=models.IntegerField(null=True),
        ),
    ]
