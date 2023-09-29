# Generated by Django 4.2.3 on 2023-09-06 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familyheaddetails',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familymembers',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
