# Generated by Django 3.0.7 on 2020-07-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_timeslotforvendor'),
        ('accounts', '0005_auto_20200718_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_profile',
            name='calendar',
            field=models.ManyToManyField(blank=True, to='engine.TimeSlot'),
        ),
    ]
