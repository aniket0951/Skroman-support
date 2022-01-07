# Generated by Django 4.0 on 2022-01-05 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('designation', models.CharField(blank=True, max_length=120, null=True)),
                ('department', models.CharField(blank=True, max_length=120, null=True)),
                ('employee_id', models.CharField(blank=True, max_length=120, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=120, null=True)),
                ('auth_token', models.CharField(blank=True, max_length=120, null=True)),
                ('status', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'skroman_login',
            },
        ),
    ]