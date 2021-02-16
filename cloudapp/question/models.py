from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from exam.models import Assignment, Exam
import datetime as dt
from enum import Enum
import pytz


class ExamStatus(Enum):
    NotStarted = " NOT STARTED"
    Open = "OPEN"
    TimesUp = "TIME'S UP"
    Completed = "COMPLETED"


def validate_choice(value):
    if value > 4:
        raise ValidationError(
            ('Index %(value)s is not a choice'),
            params={'value': value},
        )


def under100(value):
    if value > 100:
        raise ValidationError(
            ('Question point is not over 100 point'),
            params={'value': value},
        )


# Create your models here.
class Question(models.Model):
    id = CharField(max_length=20, primary_key=True, db_column='id')
    exam_id = ForeignKey(Exam,
                         default=None,
                         db_column='EXAMID',
                         on_delete=models.CASCADE)
    context = CharField(max_length=1000, default='', db_column='CONTEXT')
    choice1 = CharField(max_length=400, default='', db_column='CHOICE1')
    choice2 = CharField(max_length=400, default='', db_column='CHOICE2')
    choice3 = CharField(max_length=400, default='', db_column='CHOICE3')
    choice4 = CharField(max_length=400, default='', db_column='CHOICE4')
    correct = IntegerField(db_column='CORRECT',
                           default=1,
                           validators=[validate_choice])
    point = IntegerField(default=0, validators=[under100])

    class Meta:
        db_table = "QUESTION"


class Answer(models.Model):
    id = CharField(max_length=20, primary_key=True, db_column='id')
    question_id = ForeignKey(Question,
                             db_column='QUESTID',
                             default='',
                             on_delete=models.CASCADE)
    assignment_id = ForeignKey(Assignment,
                               db_column='ASNID',
                               default='',
                               on_delete=models.CASCADE)
    answer = IntegerField(db_column='ANSWER',
                          default=1,
                          validators=[validate_choice])

    class Meta:
        db_table = "ANSWER"
        unique_together = (("question_id", "assignment_id"), )


class CreatedQuiz:
    id = None
    org_name = None
    name = None
    start_date = None
    end_date = None

    def __init__(self, exid, name, surname, qname, start, end):
        self.id = exid
        self.org_name = name + " " + surname
        self.name = qname
        self.start_date = start
        self.end_date = end


class AssignedQuiz:
    id = None
    org_name = None
    quiz_name = None
    start_date = None
    end_date = None
    status = None

    def __init__(self, exid, name, surname, qname, start, end, stat):
        self.id = exid
        self.org_name = name + " " + surname
        utc = pytz.UTC
        self.quiz_name = qname
        self.start_date = start
        self.end_date = end
        now = utc.localize(dt.datetime.now())
        if stat == 1:
            self.status = 0
        elif start > now:
            self.status = 0
        elif start < now and end > now:
            self.status = 1
        else:
            self.status = 0
