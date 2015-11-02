# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('instacart_shopper', '0002_auto_20151031_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2015, 11, 1, 2, 28, 3, 400425, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2015, 11, 1, 2, 28, 3, 400152, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phone',
            field=models.IntegerField(unique=True, max_length=10),
        ),
    ]
