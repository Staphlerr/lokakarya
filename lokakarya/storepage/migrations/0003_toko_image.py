# Generated by Django 5.1.1 on 2024-10-26 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storepage', '0002_toko_delete_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='toko',
            name='image',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
