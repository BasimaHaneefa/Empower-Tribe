# Generated by Django 5.0.4 on 2024-04-24 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_donationtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donationtype', models.CharField(max_length=50)),
            ],
        ),
    ]