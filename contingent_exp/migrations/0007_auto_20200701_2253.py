# Generated by Django 3.0.7 on 2020-07-01 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contingent_exp', '0006_auto_20200629_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='contingent_exp',
            name='employee_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contingent_exp',
            name='Bank_account_number',
            field=models.CharField(max_length=15),
        ),
    ]