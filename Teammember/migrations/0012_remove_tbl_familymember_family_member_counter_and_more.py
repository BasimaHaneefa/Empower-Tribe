# Generated by Django 5.0.4 on 2024-04-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teammember', '0011_alter_tbl_family_teammember_alter_tbl_product_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_familymember',
            name='family_member_counter',
        ),
        migrations.AddField(
            model_name='tbl_family',
            name='family_member_count',
            field=models.CharField(max_length=50, null=True),
        ),
    ]