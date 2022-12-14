# Generated by Django 4.0.4 on 2022-06-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_content', '0003_alter_attachment_name_alter_media_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='format',
            field=models.CharField(choices=[('png', 'image/png'), ('jpg', 'image/jpg'), ('jpeg', 'image/jpeg'), ('gif', 'image/gif'), ('mp4', 'video/mp4'), ('webm', 'video/webm'), ('x-m4v', 'video/x-m4v'), ('quicktime', 'video/quicktime'), ('x-wav', 'audio/x-wav'), ('mp3', 'audio/mp3'), ('mpeg', 'audio/mpeg')], max_length=30),
        ),
    ]
