# Generated by Django 3.1.3 on 2020-11-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20201120_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='cost_of_revenue',
            field=models.CharField(default='not found', max_length=200),
        ),
        migrations.AlterField(
            model_name='stock',
            name='total_revenue',
            field=models.CharField(default='not found', max_length=200),
        ),
    ]
