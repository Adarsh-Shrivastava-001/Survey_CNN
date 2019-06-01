# Generated by Django 2.1.7 on 2019-06-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('e_mail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('part', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]