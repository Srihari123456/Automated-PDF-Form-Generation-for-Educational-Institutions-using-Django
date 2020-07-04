# Generated by Django 3.0.7 on 2020-06-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ta_bill', '0004_auto_20200627_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ta_bill',
            old_name='paid_by_iith',
            new_name='To_be_paid_by_iith',
        ),
        migrations.RenameField(
            model_name='ta_bill',
            old_name='recovered_by_iith',
            new_name='To_be_recovered_by_iith',
        ),
        migrations.RenameField(
            model_name='ta_bill',
            old_name='totamount_A',
            new_name='Total_amount_A',
        ),
        migrations.RenameField(
            model_name='ta_bill',
            old_name='totamount_B',
            new_name='Total_amount_B',
        ),
        migrations.RenameField(
            model_name='ta_bill',
            old_name='encl_date',
            new_name='enclosure_date',
        ),
        migrations.RenameField(
            model_name='ta_bill',
            old_name='no_of_encls',
            new_name='no_of_enclosures',
        ),
        migrations.AlterField(
            model_name='ta_bill',
            name='Bank_account_number',
            field=models.CharField(max_length=15),
        ),
    ]