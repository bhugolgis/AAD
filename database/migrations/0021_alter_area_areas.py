# Generated by Django 4.2.5 on 2023-09-29 10:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_alter_healthpost_healthpostname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='areas',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=1000), blank=True, null=True, size=None),
        ),
    ]
