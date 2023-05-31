# Generated by Django 4.2.1 on 2023-06-06 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mercearia', '0012_remove_mercearia_entrega_alter_mercearia_endereço_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mercearia',
            name='preco_arroz',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=6, verbose_name='Preco Arroz'),
        ),
        migrations.AddField(
            model_name='mercearia',
            name='preco_feijao',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=6, verbose_name='Preco Feijão'),
        ),
        migrations.AddField(
            model_name='mercearia',
            name='preco_refri',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=6, verbose_name='Preco Refrigerante'),
        ),
        migrations.AlterField(
            model_name='mercearia',
            name='endereço',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mercearia',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=6),
        ),
    ]