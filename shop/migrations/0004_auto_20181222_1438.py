# Generated by Django 2.1.1 on 2018-12-22 06:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181222_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='beizhu',
            field=models.CharField(db_index=True, default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sale_address',
            field=models.CharField(db_index=True, default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='youfei',
            field=models.CharField(db_index=True, default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_size',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product_color',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product_size', to_field='slug'),
        ),
    ]