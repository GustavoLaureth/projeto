# Generated by Django 4.1.7 on 2023-05-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_cliente_n_nfe_cliente_nfe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='empenho',
            field=models.FileField(max_length=500, upload_to='empenhos/'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nfe',
            field=models.FileField(blank=True, max_length=500, upload_to='notas/'),
        ),
    ]
