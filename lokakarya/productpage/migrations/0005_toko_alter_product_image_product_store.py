# Generated by Django 5.1 on 2024-10-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productpage', '0004_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('hari_buka', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telepon', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/avatars/defaults.jpeg', upload_to='static/'),
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ManyToManyField(related_name='products', to='productpage.toko'),
        ),
    ]