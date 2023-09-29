# Generated by Django 4.2.5 on 2023-09-25 13:02

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_rename_addressline1_familyheaddetails_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='phlebotomist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testReport', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('HB', 'HB'), ('CBC', 'CBC'), ('Platelet Count', 'Platelet Count'), ('PT/INR', 'PT/INR'), ('RBS', 'RBS'), ('S. Total Bilirubin', 'S. Total BilirubinB'), ('S. Direct Bilirubin', 'S. Direct Bilirubin'), ('SGPT/ALT', 'SGPT/ALT'), ('SGOT/AST', 'SGOT/AST'), ('Urea / BUN', 'Urea / BUN'), ('S. Creatinine', 'S. Creatinine'), ('ALP', 'ALP'), ('S. Total Proteins', 'S. Total Proteins'), ('S. Albumin', 'S. Albumin'), ('S. Total Calcium', 'S. Total Calcium'), ('S. Uric Acid', 'S. Uric Acid'), ('S. Cholesterol', 'S. Cholesterol'), ('S. Triglycerides ', 'S. Triglycerides '), ('S. HDL (Direct)', 'S. HDL (Direct)'), ('LDL', 'LDL'), ('VLDL', 'VLDL'), ('Amylase', 'Amylase'), ('T3', 'T3'), ('T4', 'T4'), ('HbA1C', 'HbA1C'), ('S. Electrolytes', 'S. Electrolytes'), ('S. TIBC', 'S. TIBC'), ('LDH', 'LDH'), ('Vit. D', 'Vit. D'), ('Vit. B12', 'Vit. B12'), ('Immunoassays', 'Immunoassays')], max_length=255, null=True), size=None)),
                ('barcodeNumber', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), size=None)),
                ('date', models.DateField(blank=True, null=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='family_Member', to='database.familymembers')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phlebotomist_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
