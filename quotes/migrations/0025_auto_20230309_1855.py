# Generated by Django 3.2 on 2023-03-09 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0024_alter_quotecategorydetail_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='quotecategorydetail',
            name='price',
        ),
    ]
