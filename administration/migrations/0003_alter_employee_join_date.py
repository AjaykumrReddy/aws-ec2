# Generated by Django 4.2.4 on 2023-08-04 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_alter_employee_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='join_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]