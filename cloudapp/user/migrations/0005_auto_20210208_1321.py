# Generated by Django 2.2.5 on 2021-02-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210208_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sysuser',
            name='is_organizer',
            field=models.BooleanField(db_column='is_organizer', default=False),
        ),
    ]
