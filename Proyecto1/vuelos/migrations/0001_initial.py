# Generated by Django 2.2.5 on 2019-10-18 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='airports',
            fields=[
                ('id_airport', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='pk_airport')),
                ('codigo', models.IntegerField()),
                ('ciudad', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='vuelos',
            fields=[
                ('id_vuelos', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='pk_vuelo')),
                ('duration', models.IntegerField(null=True)),
                ('id_destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_destino', to='vuelos.airports')),
                ('id_origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_origen', to='vuelos.airports')),
            ],
        ),
    ]
