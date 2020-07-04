# Generated by Django 3.0.7 on 2020-06-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_adv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('designation', models.CharField(max_length=120)),
                ('department', models.CharField(max_length=120)),
                ('employee_id', models.CharField(max_length=12)),
                ('basic_pay', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('journeyclass', models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6)),
                ('dt1', models.CharField(max_length=10)),
                ('dt2', models.CharField(max_length=10)),
                ('purpose', models.TextField()),
                ('accommodation_charges', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('other_expenditures', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('details', models.CharField(max_length=120)),
                ('totamount', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('IFSC_Code', models.CharField(max_length=12)),
                ('Bank_name_branch', models.TextField()),
                ('Bank_account_number', models.TextField()),
            ],
        ),
    ]