# Generated by Django 5.0.4 on 2024-04-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_tbl_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_booking',
            name='booking_totalamount',
            field=models.CharField(max_length=50, null=True),
        ),
    ]