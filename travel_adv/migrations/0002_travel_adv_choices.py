# Generated by Django 3.0.7 on 2020-06-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_adv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_adv_choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=120)),
            ],
        ),
    ]