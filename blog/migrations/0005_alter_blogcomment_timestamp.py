# Generated by Django 4.2.6 on 2023-11-10 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogcomment_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='timeStamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 10, 12, 18, 14, 34500)),
        ),
    ]
