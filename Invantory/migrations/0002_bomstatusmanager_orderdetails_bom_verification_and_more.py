# Generated by Django 4.0 on 2022-01-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invantory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOMStatusManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_name', models.CharField(blank=True, max_length=210, null=True)),
                ('verification_status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'bom_status_manager',
            },
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='bom_verification',
            field=models.CharField(blank=True, max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='bom_verification',
            field=models.CharField(blank=True, max_length=210, null=True),
        ),
    ]
