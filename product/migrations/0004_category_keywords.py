# Generated by Django 4.0.3 on 2022-03-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
