# Generated by Django 5.0 on 2023-12-22 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Portfolio Name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Portfolio Email')),
                ('phone_number', models.CharField(blank=True, max_length=30, verbose_name='Portfolio Phone Number')),
                ('professional', models.CharField(blank=True, max_length=50, verbose_name='Professional')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Portfolio Address')),
                ('avator', models.ImageField(blank=True, upload_to='portfolio/', verbose_name='Portfolio Avator')),
                ('about', models.TextField(verbose_name='Portfolio About')),
                ('available_status', models.BooleanField(default=1, verbose_name='Portfolio Available')),
                ('status', models.BooleanField(default=0, verbose_name='Portfolio Status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated Time')),
            ],
        ),
    ]
