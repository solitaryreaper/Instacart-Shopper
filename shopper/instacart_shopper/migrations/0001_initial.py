# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('phone', models.IntegerField(unique=True)),
                ('location', models.CharField(max_length=100)),
                ('workflow_state', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
            ],
        ),
    ]
