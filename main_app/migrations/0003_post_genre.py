# Generated by Django 3.0.7 on 2020-06-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200620_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JS', 'JavaScript'), ('UX', 'UX Design'), ('PI', 'Project Ideas')], default='HTML', max_length=4),
        ),
    ]
