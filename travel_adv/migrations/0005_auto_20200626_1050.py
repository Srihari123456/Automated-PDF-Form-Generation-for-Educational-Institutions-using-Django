# Generated by Django 3.0.7 on 2020-06-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_adv', '0004_auto_20200626_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel_adv',
            name='accommodation_charges',
            field=models.DecimalField(decimal_places=2, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='travel_adv',
            name='journeyclass',
            field=models.CharField(choices=[('Air(Business)', 'Air(Business)'), ('Air(Economy)', 'Air(Economy)'), ('Train(1AC)', 'Train(1AC)'), ('Train(2AC)', 'Train(2AC)'), ('Train(3AC)', 'Train(3AC)'), ('Train(ACC)', 'Train(ACC)'), ('Train(SL)', 'Train(SL)'), ('Train(CC)', 'Train(CC)'), ('Road (AC)', 'Road (AC)'), ('Road (Non-AC)', 'Road (Non-AC)')], default='Road (AC)', max_length=60),
        ),
    ]