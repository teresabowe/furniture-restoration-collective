# Generated by Django 3.2 on 2023-03-09 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0020_remove_quote_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quotecategorydetail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quotes.quotecategorydetail'),
        ),
    ]
