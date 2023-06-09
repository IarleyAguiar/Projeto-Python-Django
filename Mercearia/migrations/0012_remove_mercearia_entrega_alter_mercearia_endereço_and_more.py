# Generated by Django 4.2.1 on 2023-06-06 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mercearia', '0011_alter_mercearia_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mercearia',
            name='entrega',
        ),
        migrations.AlterField(
            model_name='mercearia',
            name='endereço',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mercearia',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=5),
        ),
    ]
