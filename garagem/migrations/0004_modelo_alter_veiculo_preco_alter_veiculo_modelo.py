# Generated by Django 4.1.7 on 2023-03-31 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0003_veiculo_modelo_alter_veiculo_preco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.modelo'),
        ),
    ]
