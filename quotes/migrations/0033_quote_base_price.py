# Generated by Django 3.2 on 2023-03-10 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0032_remove_quote_base_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='base_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='price_detail', to='quotes.quotecategorydetail'),
        ),
    ]
