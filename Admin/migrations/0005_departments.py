# Generated by Django 4.0 on 2022-01-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_processdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(blank=True, max_length=120, null=True)),
                ('dept_id', models.CharField(blank=True, max_length=120, null=True)),
                ('dept_head', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
    ]
