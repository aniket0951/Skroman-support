# Generated by Django 4.0 on 2022-01-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0010_leadnotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadnotes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
