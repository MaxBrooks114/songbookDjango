# Generated by Django 3.0.8 on 2020-07-20 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200720_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrument',
            name='user',
        ),
        migrations.RemoveField(
            model_name='song',
            name='user',
        ),
    ]