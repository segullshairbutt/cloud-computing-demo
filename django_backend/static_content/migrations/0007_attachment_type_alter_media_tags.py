# Generated by Django 4.0.4 on 2022-06-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_content', '0006_alter_media_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='type',
            field=models.CharField(blank=True, choices=[('image', 'image'), ('image', 'image'), ('video', 'video'), ('video', 'video'), ('audio', 'audio'), ('audio', 'audio'), ('document', 'document'), ('document', 'document')], max_length=10),
        ),
        migrations.AlterField(
            model_name='media',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='media', to='static_content.tag'),
        ),
    ]