# Generated by Django 2.2.6 on 2020-02-13 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0032_slider_projname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagenext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('urljpg', models.CharField(blank=True, max_length=100)),
                ('textup', models.TextField(blank=True)),
                ('quote', models.TextField(blank=True)),
                ('textdown', models.TextField(blank=True)),
                ('urlvideo', models.CharField(blank=True, max_length=100)),
                ('blockquote', models.TextField(blank=True)),
                ('paragraph', models.TextField(blank=True)),
                ('titlenext', models.CharField(blank=True, max_length=30)),
                ('textnext', models.TextField(blank=True)),
                ('projname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subnext', to='information.Subnavigator')),
                ('subname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next', to='information.Navconstruct')),
            ],
        ),
    ]
