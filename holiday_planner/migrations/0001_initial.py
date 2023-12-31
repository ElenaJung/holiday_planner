# Generated by Django 4.2.7 on 2023-11-05 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.CharField(max_length=36)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'indexes': [models.Index(fields=['owner_id'], name='holiday_pla_owner_i_f03d2f_idx')],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holiday_planner.trip')),
            ],
            options={
                'indexes': [models.Index(fields=['trip'], name='holiday_pla_trip_id_154416_idx')],
            },
        ),
    ]
