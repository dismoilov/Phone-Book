# Generated by Django 5.0.2 on 2024-02-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_call_status_alter_call_recording'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='recording',
            field=models.FileField(upload_to='recordings'),
        ),
    ]
