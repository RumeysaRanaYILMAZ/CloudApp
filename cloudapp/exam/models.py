from django import db
from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
from user.models import SysUser
# Create your models here.


class Exam(models.Model):
    id = CharField(max_length=20,
                   primary_key=True,
                   db_column='EXAMID',
                   auto_created=True)
    name = CharField(max_length=100, db_column='EXNAME')
    organizer = ForeignKey(SysUser,
                           default=None,
                           db_column='ORGANIZER',
                           on_delete=models.CASCADE)
    start_time = DateTimeField(db_column='START')
    end_time = DateTimeField(db_column='END')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "EXAM"


class Assignment(models.Model):
    username = ForeignKey(SysUser,
                          db_column='STUDENT',
                          on_delete=models.CASCADE)
    exam_id = ForeignKey(Exam, db_column='EXAMID', on_delete=models.CASCADE)

    class Meta:
        db_table = "ASSIGNMENT"
        unique_together = (("username", "exam_id"), )
