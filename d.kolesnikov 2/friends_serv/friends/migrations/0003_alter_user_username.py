# Generated by Django 4.2.1 on 2023-05-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_friendrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
