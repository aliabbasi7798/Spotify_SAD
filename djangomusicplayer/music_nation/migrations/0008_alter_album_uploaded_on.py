# Generated by Django 3.2.5 on 2021-07-25 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0007_alter_album_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2021, 7, 25, 21, 37, 40, 398446)),
        ),
    ]