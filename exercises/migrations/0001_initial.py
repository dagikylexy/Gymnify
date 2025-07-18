# Generated by Django 5.1.2 on 2025-07-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20)),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caloriesPerRep', models.FloatField()),
                ('description', models.TextField()),
                ('equipment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('chest', 'Chest'), ('back', 'Back'), ('shoulders', 'Shoulders'), ('arms', 'Arms'), ('biceps', 'Biceps'), ('triceps', 'Triceps'), ('core', 'Core'), ('legs', 'Legs')], max_length=20)),
                ('caloriesPerRep', models.FloatField()),
                ('image', models.CharField(max_length=255)),
                ('video', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('timeTaken', models.CharField(blank=True, max_length=50, null=True)),
                ('requireKG', models.JSONField(blank=True, null=True)),
                ('effectiveness', models.IntegerField()),
                ('activityLevels', models.JSONField()),
                ('equipment', models.BooleanField(default=False)),
                ('primaryMuscles', models.JSONField()),
                ('secondaryMuscles', models.JSONField()),
                ('alternatives', models.ManyToManyField(to='exercises.alternative')),
            ],
        ),
    ]
