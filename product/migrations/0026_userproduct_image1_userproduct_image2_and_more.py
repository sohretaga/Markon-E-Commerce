# Generated by Django 4.0.3 on 2022-04-17 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_userproduct_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproduct',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='static/product_images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='userproduct',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/product_images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='userproduct',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='static/product_images/%Y/%m/%d/'),
        ),
    ]
