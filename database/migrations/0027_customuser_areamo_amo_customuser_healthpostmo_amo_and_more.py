# Generated by Django 4.2.6 on 2023-10-16 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0026_familyheaddetails_islabtestadded_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='areaMo_Amo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='areaAmo_mo_name', to='database.ward'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='healthPostMo_Amo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='healthpostAmo_mo_name', to='database.ward'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='wardMo_Amo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wardAmo_mo_name', to='database.ward'),
        ),
    ]