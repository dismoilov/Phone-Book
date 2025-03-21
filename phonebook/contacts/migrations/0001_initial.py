# Generated by Django 5.0.2 on 2025-03-14 14:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Главная категория')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DisplayName', models.CharField(max_length=50)),
                ('OfficeNumber', models.CharField(max_length=10, unique=True)),
                ('MobileNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('OtherNumber', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CallSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Подкатегория')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='contacts.callcategory', verbose_name='Главная категория')),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_id', models.CharField(max_length=50, unique=True, verbose_name='ID звонка')),
                ('caller', models.CharField(max_length=20, verbose_name='Номер звонящего')),
                ('receiver', models.CharField(max_length=20, verbose_name='Номер получателя')),
                ('call_type', models.CharField(choices=[('incoming', 'Входящий'), ('outgoing', 'Исходящий'), ('local', 'Локальный')], max_length=10, verbose_name='Тип звонка')),
                ('duration', models.PositiveIntegerField(blank=True, null=True, verbose_name='Длительность (сек)')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата звонка')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Время звонка')),
                ('recording', models.FileField(blank=True, null=True, upload_to='recordings', verbose_name='Запись звонка')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.callcategory', verbose_name='Категория')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.callsubcategory', verbose_name='Подкатегория')),
            ],
        ),
    ]
