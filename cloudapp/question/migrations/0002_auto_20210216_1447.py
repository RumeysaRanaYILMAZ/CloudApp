# Generated by Django 2.2.5 on 2021-02-16 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20210212_1035'),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='assingment_id',
            new_name='assignment_id',
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question_id', 'assignment_id')},
        ),
    ]
