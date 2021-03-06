# Generated by Django 2.1.7 on 2019-06-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0005_auto_20190601_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='correct',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='incorrect',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='neither',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='rel_corr',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='rel_wrong',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
