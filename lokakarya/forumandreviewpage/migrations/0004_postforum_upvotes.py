# Generated by Django 5.1.2 on 2024-10-25 04:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumandreviewpage', '0003_remove_postforum_upvotes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='postforum',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='post_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]