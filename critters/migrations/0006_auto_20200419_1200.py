# Generated by Django 3.0.5 on 2020-04-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('critters', '0005_auto_20200418_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='entity_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fish',
            name='entity_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bug',
            name='all_day',
            field=models.BooleanField(default=False),
        ),
    ]