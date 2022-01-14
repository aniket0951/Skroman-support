# Generated by Django 4.0 on 2022-01-14 09:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0006_leadreferances_ref_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprojectdetails',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientprojectdetails',
            name='uptime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='leadreferances',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leadreferances',
            name='uptime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]