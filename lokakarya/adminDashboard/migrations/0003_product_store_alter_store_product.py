# Generated by Django 5.1 on 2024-10-25 04:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminDashboard', '0002_category_rating_remove_product_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='adminDashboard.store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='product',
            field=models.ManyToManyField(related_name='stores', to='adminDashboard.product'),
        ),
    ]