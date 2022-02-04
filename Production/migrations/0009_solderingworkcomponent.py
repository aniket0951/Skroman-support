# Generated by Django 4.0 on 2022-02-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0008_completedtask_device_id_completedtask_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolderingWorkComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=40, null=True)),
                ('model_name', models.CharField(blank=True, max_length=40, null=True)),
                ('pcb_type', models.CharField(blank=True, max_length=260, null=True)),
            ],
            options={
                'db_table': 'soldering_work_component',
            },
        ),
    ]