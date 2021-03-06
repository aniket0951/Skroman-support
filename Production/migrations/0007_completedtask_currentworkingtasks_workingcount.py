# Generated by Django 4.0 on 2022-01-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0006_productionuser_auth_token_productionuser_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(blank=True, max_length=140, null=True)),
                ('task_name', models.CharField(blank=True, max_length=140, null=True)),
                ('task_id', models.CharField(blank=True, max_length=140, null=True)),
                ('task_date', models.CharField(blank=True, max_length=140, null=True)),
                ('task_status', models.CharField(blank=True, max_length=10, null=True)),
                ('task_time', models.CharField(blank=True, max_length=140, null=True)),
            ],
            options={
                'db_table': 'completed_working_task',
            },
        ),
        migrations.CreateModel(
            name='CurrentWorkingTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(blank=True, max_length=140, null=True)),
                ('task_name', models.CharField(blank=True, max_length=140, null=True)),
                ('task_id', models.CharField(blank=True, max_length=140, null=True)),
                ('task_date', models.CharField(blank=True, max_length=140, null=True)),
                ('task_status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'current_working_task',
            },
        ),
        migrations.CreateModel(
            name='WorkingCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(blank=True, max_length=140, null=True)),
                ('working_date', models.CharField(blank=True, max_length=140, null=True)),
                ('task_count', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'working_count',
            },
        ),
    ]
