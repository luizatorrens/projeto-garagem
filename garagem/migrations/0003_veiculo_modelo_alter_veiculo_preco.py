# Generated by Django 4.1.7 on 2023-03-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0002_acessorio_cor_veiculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='modelo',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=7, null=True),
        ),
    ]
