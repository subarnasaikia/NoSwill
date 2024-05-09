# Generated by Django 5.0.6 on 2024-05-09 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='invetoryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(blank=True, max_length=10, null=True)),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('item_stock', models.IntegerField(blank=True, null=True)),
                ('item_experey_date', models.DateField(blank=True, null=True)),
                ('item_created_at', models.DateTimeField(auto_now_add=True)),
                ('item_modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]