# Generated by Django 3.1.6 on 2021-10-17 14:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0010_auto_20211017_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='executedTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 14, 48, 22, 128386, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='registeredTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 14, 48, 22, 128301, tzinfo=utc)),
        ),
    ]
