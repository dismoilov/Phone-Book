# Generated by Django 4.2.3 on 2023-07-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DisplayName', models.CharField(max_length=50)),
                ('OfficeNumber', models.CharField(max_length=10)),
                ('MobileNumber', models.CharField(max_length=15)),
                ('OtherNumber', models.CharField(max_length=15)),
            ],
        ),
    ]