# Generated by Django 3.1.6 on 2021-10-17 14:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0008_auto_20211017_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='executedTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 14, 46, 46, 837153, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='registeredTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 14, 46, 46, 837115, tzinfo=utc)),
        ),
    ]
