# Generated by Django 5.0.2 on 2024-02-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_call'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='status',
            field=models.CharField(choices=[('Inbound', 'Входящий'), ('Outbound', 'Исходящий'), ('Local', 'Локальный')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='recording',
            field=models.CharField(max_length=250),
        ),
    ]
