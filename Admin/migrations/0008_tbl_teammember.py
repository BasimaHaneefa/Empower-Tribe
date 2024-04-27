# Generated by Django 5.0.4 on 2024-04-27 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_tbl_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_teammember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('member_contact', models.CharField(max_length=50)),
                ('member_email', models.CharField(max_length=50)),
                ('member_address', models.CharField(max_length=50)),
                ('member_photo', models.FileField(upload_to='Memberdoc/')),
                ('member_proof', models.FileField(upload_to='Memberdoc/')),
                ('member_password', models.CharField(max_length=50)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_team')),
            ],
        ),
    ]