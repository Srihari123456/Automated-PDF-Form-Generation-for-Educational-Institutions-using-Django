# Generated by Django 3.0.7 on 2020-07-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reimbursement', '0005_auto_20200701_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reimbursement',
            name='Bank_account_number',
            field=models.CharField(max_length=16),
        ),
    ]