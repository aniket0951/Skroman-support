# Generated by Django 4.0 on 2022-01-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0003_clientdetails_c_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetails',
            name='c_site_address',
            field=models.CharField(blank=True, max_length=460, null=True),
        ),
    ]
