# Generated by Django 4.2.6 on 2023-10-16 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0031_customuser_dispensary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='healthPostMo_Amo',
            new_name='healthPost',
        ),
    ]
