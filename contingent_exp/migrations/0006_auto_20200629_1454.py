# Generated by Django 3.0.7 on 2020-06-29 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contingent_exp', '0005_auto_20200625_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contingent_exp',
            old_name='totamount',
            new_name='Total_amount',
        ),
    ]
