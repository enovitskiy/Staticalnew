# Generated by Django 2.1 on 2020-03-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0062_etapy_href1'),
    ]

    operations = [
        migrations.AddField(
            model_name='etapy',
            name='answernext',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='etapy',
            name='href',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='etapy',
            name='namenext',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
