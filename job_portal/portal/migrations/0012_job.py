# Generated by Django 5.2.1 on 2025-06-15 07:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_student_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(default='N/A', max_length=100)),
                ('job_description', models.TextField(default='N/A')),
                ('job_location', models.CharField(default='N/A', max_length=100)),
                ('job_type', models.CharField(default='Full Time', max_length=50)),
                ('job_skills_required', models.CharField(default='N/A', max_length=100)),
                ('job_salary', models.CharField(default='N/A', max_length=50)),
                ('job_posted_on', models.DateField(auto_now_add=True)),
                ('job_last_date', models.DateField(blank=True, null=True)),
                ('job_contact_email', models.EmailField(default='N/A', max_length=100)),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='portal.company')),
            ],
            options={
                'db_table': 'job',
            },
        ),
    ]
