# Generated by Django 3.0.5 on 2020-06-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]
