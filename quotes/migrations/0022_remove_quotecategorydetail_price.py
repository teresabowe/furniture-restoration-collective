# Generated by Django 3.2 on 2023-03-09 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0021_alter_quote_quotecategorydetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotecategorydetail',
            name='price',
        ),
    ]
