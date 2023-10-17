# Generated by Django 4.2.5 on 2023-10-17 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_tertiaryconsultancy_secondaryconsultancy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispensary',
            name='disphealthPost',
        ),
        migrations.AddField(
            model_name='healthpost',
            name='dispensary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispensarys_name', to='database.dispensary'),
        ),
    ]