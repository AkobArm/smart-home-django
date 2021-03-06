# Generated by Django 3.2.9 on 2021-11-30 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Measurement',
        ),
        migrations.AddField(
            model_name='sensor',
            name='measurements',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='measurement.measurements'),
        ),
    ]
