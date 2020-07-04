# Generated by Django 3.0.7 on 2020-06-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TA_Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('employee_id', models.CharField(max_length=12)),
                ('designation', models.CharField(max_length=120)),
                ('department', models.CharField(max_length=120)),
                ('institute', models.CharField(max_length=120)),
                ('basicpay', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('institute_acc_no', models.CharField(max_length=120)),
                ('purpose', models.TextField()),
                ('dep_station_1', models.CharField(max_length=120)),
                ('dep_date_1', models.TextField(max_length=10)),
                ('arr_station_1', models.CharField(max_length=120)),
                ('arr_date_1', models.TextField(max_length=10)),
                ('mode_of_journey_1', models.CharField(choices=[('Air', 'Air'), ('Rail', 'Rail'), ('Road', 'Road'), ('-', '-')], default='-', max_length=60)),
                ('ticket_no_1', models.CharField(max_length=120)),
                ('fare_1', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('dep_station_2', models.CharField(max_length=120)),
                ('dep_date_2', models.TextField(blank=True, max_length=10, null=True)),
                ('arr_station_2', models.CharField(max_length=120)),
                ('arr_date_2', models.TextField(blank=True, max_length=10, null=True)),
                ('mode_of_journey_2', models.CharField(choices=[('Air', 'Air'), ('Rail', 'Rail'), ('Road', 'Road'), ('-', '-')], default='-', max_length=60)),
                ('ticket_no_2', models.CharField(max_length=120)),
                ('fare_2', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('dep_station_3', models.CharField(max_length=120)),
                ('dep_date_3', models.TextField(blank=True, max_length=10, null=True)),
                ('arr_station_3', models.CharField(max_length=120)),
                ('arr_date_3', models.TextField(blank=True, max_length=10, null=True)),
                ('mode_of_journey_3', models.CharField(choices=[('Air', 'Air'), ('Rail', 'Rail'), ('Road', 'Road'), ('-', '-')], default='-', max_length=60)),
                ('ticket_no_3', models.CharField(max_length=120)),
                ('fare_3', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('totamount_A', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('other_exp_item_1', models.CharField(max_length=120)),
                ('other_exp_amount_1', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('other_exp_billdetails_1', models.CharField(max_length=120)),
                ('other_exp_item_2', models.CharField(max_length=120)),
                ('other_exp_amount_2', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('other_exp_billdetails_2', models.CharField(max_length=120)),
                ('other_exp_item_3', models.CharField(max_length=120)),
                ('other_exp_amount_3', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('other_exp_billdetails_3', models.CharField(max_length=120)),
                ('totamount_B', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('no_of_encls', models.IntegerField()),
                ('encl_date', models.TextField(max_length=10)),
                ('Admissible_Amount', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('AdvanceDraw', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('Net_Claim_Admissible', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('paid_by_iith', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('recovered_by_iith', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('payment_voucher_no', models.CharField(max_length=120)),
                ('pymt_date', models.TextField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('amt_in_words', models.CharField(max_length=120)),
                ('IFSC_Code', models.CharField(max_length=12)),
                ('Bank_name_branch', models.TextField()),
                ('Bank_account_number', models.TextField()),
            ],
        ),
    ]
