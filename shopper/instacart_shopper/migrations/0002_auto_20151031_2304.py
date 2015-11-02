# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instacart_shopper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='workflow_state',
            field=models.CharField(default=b'applied', max_length=100),
        ),
    ]
