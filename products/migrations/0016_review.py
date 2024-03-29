# Generated by Django 3.2 on 2023-04-11 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=3)),
                ('crafter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.crafter')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
