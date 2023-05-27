# Generated by Django 4.1.7 on 2023-05-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_alter_drug_medical_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='activity',
            field=models.CharField(blank=True, max_length=50, verbose_name='activity'),
        ),
        migrations.AlterField(
            model_name='drug',
            name='side_effects',
            field=models.TextField(blank=True, verbose_name='Side Effects'),
        ),
    ]
