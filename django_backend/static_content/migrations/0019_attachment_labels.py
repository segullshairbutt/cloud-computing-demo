# Generated by Django 4.0.4 on 2022-08-28 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_content', '0018_alter_ratings_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='labels',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
