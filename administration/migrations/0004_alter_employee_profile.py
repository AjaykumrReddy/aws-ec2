# Generated by Django 4.2.4 on 2023-08-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_alter_employee_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile',
            field=models.ImageField(upload_to='profiles'),
        ),
    ]
