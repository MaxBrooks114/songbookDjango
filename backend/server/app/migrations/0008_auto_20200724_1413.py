# Generated by Django 3.0.8 on 2020-07-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200724_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
