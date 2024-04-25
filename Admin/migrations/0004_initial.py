# Generated by Django 5.0.4 on 2024-04-24 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0003_delete_tbl_localbody_delete_tbl_localbodytype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_localbodytype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localbodytype_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_localbody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localbody', models.CharField(max_length=50)),
                ('localbodytype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_localbodytype')),
            ],
        ),
    ]
