from django import db
from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField
from django.db.models.fields.related import ForeignKey
from user.models import User
# Create your models here.


class Exam(models.Model):
    id = CharField(max_length=20, primary_key=True, db_column='id')
    name = CharField(max_length=100, db_column='EXNAME')
    organizer = ForeignKey(User,
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
    id = CharField(max_length=20, primary_key=True, db_column='id')
    user_id = ForeignKey(User, db_column='STUDENT', on_delete=models.CASCADE)
    exam_id = ForeignKey(Exam, db_column='EXAMID', on_delete=models.CASCADE)

    result = IntegerField(db_column='RESULT', default=0)

    class Meta:
        db_table = "ASSIGNMENT"
        unique_together = (("user_id", "exam_id"), )
