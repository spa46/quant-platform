# Generated by Django 5.2.4 on 2025-07-13 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('ticker', models.CharField(max_length=32)),
                ('region', models.CharField(max_length=8)),
                ('etf', models.CharField(blank=True, max_length=32, null=True)),
                ('timezone', models.CharField(blank=True, max_length=32, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=16)),
                ('region', models.CharField(max_length=8)),
                ('timezone', models.CharField(blank=True, max_length=32, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('indexes', models.ManyToManyField(blank=True, related_name='tickers', to='stocks.index')),
            ],
        ),
        migrations.CreateModel(
            name='TickerDailyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('open', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('close', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('low', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('volume', models.BigIntegerField(blank=True, null=True)),
                ('per', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('dividend', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('capital', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('analyst_feeds', models.JSONField(blank=True, null=True)),
                ('extra_data', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.ticker')),
            ],
            options={
                'ordering': ['-date', 'ticker'],
                'unique_together': {('ticker', 'date')},
            },
        ),
    ]
