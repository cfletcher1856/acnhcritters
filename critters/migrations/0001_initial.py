# Generated by Django 3.0.5 on 2020-04-18 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image_64', models.TextField()),
                ('image_url', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=200)),
                ('start_time', models.IntegerField(default=0)),
                ('end_time', models.IntegerField(default=0)),
                ('all_day', models.BooleanField()),
                ('active_time', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image_64', models.TextField()),
                ('image_url', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=200)),
                ('start_time', models.IntegerField(default=0)),
                ('end_time', models.IntegerField(default=0)),
                ('all_day', models.BooleanField()),
                ('active_time', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ActiveMonths',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='critters.Bug')),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='critters.Fish')),
            ],
        ),
    ]