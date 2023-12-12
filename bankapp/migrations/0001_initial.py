# Generated by Django 4.2.7 on 2023-11-22 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('addhar_number', models.IntegerField(blank=True, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('confirm_password', models.CharField(blank=True, max_length=20, null=True)),
                ('account_type', models.CharField(blank=True, max_length=20, null=True)),
                ('account_number', models.IntegerField(blank=True, null=True)),
                ('account_balance', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='reccuring_account_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('ammount', models.FloatField(default=0)),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='card_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(blank=True, max_length=10, null=True)),
                ('cvv_number', models.IntegerField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='account_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_balance', models.FloatField(blank=True, null=True)),
                ('current_balance', models.FloatField(blank=True, null=True)),
                ('account_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.user')),
            ],
        ),
    ]