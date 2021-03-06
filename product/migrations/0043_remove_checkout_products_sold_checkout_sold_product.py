# Generated by Django 4.0.4 on 2022-06-10 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0042_sold_checkout_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='products',
        ),
        migrations.AddField(
            model_name='sold',
            name='checkout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.checkout'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sold',
            name='product',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
