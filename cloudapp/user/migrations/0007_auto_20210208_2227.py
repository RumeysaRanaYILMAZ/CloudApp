# Generated by Django 2.2.5 on 2021-02-08 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210208_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysuser',
            name='saltkey',
            field=models.BinaryField(db_column='saltkey', default=b''),
        ),
        migrations.AlterField(
            model_name='sysuser',
            name='password',
            field=models.BinaryField(db_column='password', default=b''),
        ),
    ]
