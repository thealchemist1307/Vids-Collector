# Generated by Django 3.0.5 on 2020-05-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linksmodel',
            name='src',
            field=models.CharField(default='None', max_length=400),
        ),
        migrations.AddField(
            model_name='linksmodel',
            name='thumbnail_src',
            field=models.CharField(default='None', max_length=400),
        ),
    ]
