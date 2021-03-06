# Generated by Django 2.1.1 on 2018-12-22 06:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20181222_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_color',
            name='size',
        ),
        migrations.AddField(
            model_name='product_color',
            name='name',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='shop.Product', to_field='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_color',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
