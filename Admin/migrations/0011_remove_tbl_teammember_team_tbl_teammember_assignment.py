# Generated by Django 5.0.4 on 2024-04-27 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_tbl_assigmment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_teammember',
            name='team',
        ),
        migrations.AddField(
            model_name='tbl_teammember',
            name='assignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_assigmment'),
        ),
    ]
