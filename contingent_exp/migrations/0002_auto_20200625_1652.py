# Generated by Django 3.0.7 on 2020-06-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contingent_exp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contingent_exp',
            name='DateN',
        ),
        migrations.AddField(
            model_name='contingent_exp',
            name='sectio',
            field=models.CharField(default=2009, max_length=10),
            preserve_default=False,
        ),
    ]