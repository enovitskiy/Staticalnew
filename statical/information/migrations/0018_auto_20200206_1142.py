# Generated by Django 2.2.6 on 2020-02-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0017_auto_20200206_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='classdir',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='footer',
            name='hreflogo',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
