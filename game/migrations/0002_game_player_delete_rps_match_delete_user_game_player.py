# Generated by Django 5.0.3 on 2024-03-22 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_at', models.DateTimeField(auto_now_add=True)),
                ('result', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_visit', models.DateTimeField(auto_now_add=True)),
                ('nickname', models.CharField(max_length=255, null=True)),
                ('IP', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('points', models.PositiveSmallIntegerField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='rps_match',
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.player'),
        ),
    ]
