# Generated by Django 3.2 on 2023-03-19 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, limit_choices_to={'name': 'chairs'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
    ]
