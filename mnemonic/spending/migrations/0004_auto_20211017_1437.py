# Generated by Django 3.1.6 on 2021-10-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0003_transaction_registeredtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='registeredTime',
        ),
        migrations.AddField(
            model_name='transaction',
            name='cashAmount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='transaction',
            name='success',
            field=models.BooleanField(default=False),
        ),
    ]