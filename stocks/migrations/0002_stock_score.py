# Generated by Django 3.1.3 on 2020-11-20 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
