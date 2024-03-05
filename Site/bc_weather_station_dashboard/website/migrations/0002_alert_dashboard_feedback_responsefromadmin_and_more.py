# Generated by Django 5.0.2 on 2024-03-05 06:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_name', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
                ('alert_type', models.CharField(max_length=200)),
                ('alert_active', models.BooleanField()),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(default='default', max_length=200)),
                ('layout', models.CharField(choices=[('firefighter', 'Firefighter Layout'), ('common', 'Common Layout')], default='common', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('SUB', 'Submitted'), ('REV', 'In Review'), ('ADD', 'Addressed')], default='SUB', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='ResponseFromAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to=settings.AUTH_USER_MODEL)),
                ('feedback', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='website.feedback')),
            ],
        ),
        migrations.CreateModel(
            name='StationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at_timestamp', models.DateTimeField(auto_now_add=True)),
                ('STATION_CODE', models.IntegerField()),
                ('STATION_NAME', models.CharField(max_length=200)),
                ('DATE_TIME', models.DateTimeField()),
                ('HOURLY_PRECIPITATION', models.FloatField()),
                ('HOURLY_TEMPERATURE', models.FloatField()),
                ('HOURLY_RELATIVE_HUMIDITY', models.FloatField()),
                ('HOURLY_WIND_SPEED', models.FloatField()),
                ('HOURLY_WIND_DIRECTION', models.FloatField()),
                ('HOURLY_WIND_GUST', models.FloatField()),
                ('HOURLY_FINE_FUEL_MOISTURE_CODE', models.FloatField()),
                ('HOURLY_INITIAL_SPREAD_INDEX', models.FloatField()),
                ('HOURLY_FIRE_WEATHER_INDEX', models.FloatField()),
                ('PRECIPITATION', models.FloatField()),
                ('FINE_FUEL_MOISTURE_CODE', models.FloatField()),
                ('INITIAL_SPREAD_INDEX', models.FloatField()),
                ('FIRE_WEATHER_INDEX', models.FloatField()),
                ('DUFF_MOISTURE_CODE', models.FloatField()),
                ('DROUGHT_CODE', models.FloatField()),
                ('BUILDUP_INDEX', models.FloatField()),
                ('DANGER_RATING', models.FloatField()),
                ('RN_1_PLUVIO1', models.FloatField()),
                ('SNOW_DEPTH', models.FloatField()),
                ('SNOW_DEPTH_QUALITY', models.FloatField()),
                ('PRECIP_PLUVIO1_STATUS', models.FloatField()),
                ('PRECIP_PLUVIO1_TOTAL', models.FloatField()),
                ('RN_1_PLUVIO2', models.FloatField()),
                ('PRECIP_PLUVIO2_STATUS', models.FloatField()),
                ('PRECIP_PLUVIO2_TOTAL', models.FloatField()),
                ('RN_1_RIT', models.FloatField()),
                ('PRECIP_RIT_STATUS', models.FloatField()),
                ('PRECIP_RIT_TOTAL', models.FloatField()),
                ('PRECIP_RGT', models.FloatField()),
                ('SOLAR_RADIATION_LICOR', models.FloatField()),
                ('SOLAR_RADIATION_CM3', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('CU', 'Common user'), ('FS', 'Fire related staff')], default='CU', max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RenameField(
            model_name='weatherstation',
            old_name='date_time',
            new_name='INSTALL_DATE',
        ),
        migrations.RenameField(
            model_name='weatherstation',
            old_name='station_code',
            new_name='WEATHER_STATIONS_ID',
        ),
        migrations.RenameField(
            model_name='weatherstation',
            old_name='buildup_index',
            new_name='X',
        ),
        migrations.RenameField(
            model_name='weatherstation',
            old_name='danger_rating',
            new_name='Y',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='drought_code',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='duff_moisture_code',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='fine_fuel_moisture_code',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='fire_weather_index',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='hourly_fine_fuel_moisture_code',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='hourly_fire_weather_index',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='hourly_initial_spread_index',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='hourly_precipitation',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='hourly_relative_humidity',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='hourly_temperature',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='hourly_wind_direction',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='hourly_wind_gust',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='hourly_wind_speed',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='initial_spread_index',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='precip_pluvio1_status',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='precip_pluvio1_total',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='precip_pluvio2_status',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='precip_pluvio2_total',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='precip_rgt',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='precip_rit_status',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='precip_rit_total',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='precipitation',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='rn_1_pluvio1',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='rn_1_pluvio2',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='rn_1_rit',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='snow_depth',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='snow_depth_quality',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='solar_radiation_cm3',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='solar_radiation_licor',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='station_name',
        ),
        migrations.AddField(
            model_name='weatherstation',
            name='ELEVATION',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='weatherstation',
            name='STATION_ACRONYM',
            field=models.CharField(default='ST', max_length=200),
        ),
        migrations.AddField(
            model_name='weatherstation',
            name='STATION_CODE',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stationdata',
            name='station',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='station_data', to='website.weatherstation'),
        ),
        migrations.AddField(
            model_name='alert',
            name='station_data',
            field=models.ManyToManyField(to='website.stationdata'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favorite_stations',
            field=models.ManyToManyField(related_name='users', to='website.weatherstation'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='weatherstation',
            name='STATION_NAME',
            field=models.CharField(default='Station', max_length=200),
        ),
    ]
