# Generated by Django 5.0.6 on 2024-05-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeuser',
            name='hours',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
