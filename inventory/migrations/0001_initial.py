# Generated by Django 4.2.23 on 2025-07-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('product_code', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(default=0)),
                ('gst', models.IntegerField(default=0)),
            ],
        ),
    ]
