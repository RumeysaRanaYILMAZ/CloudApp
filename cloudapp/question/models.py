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


def validate_choice(value):
    if value > 4:
        raise ValidationError(
            ('Index %(value)s is not a choice'),
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

    class Meta:
        db_table = "QUESTION"


class Answer(models.Model):
    id = CharField(max_length=20, primary_key=True, db_column='id')
    question_id = ForeignKey(Question,
                             db_column='QUESTID',
                             default='',
                             on_delete=models.CASCADE)
    assingment_id = ForeignKey(Assignment,
                               db_column='ASNID',
                               default='',
                               on_delete=models.CASCADE)
    answer = IntegerField(db_column='ANSWER',
                          default=1,
                          validators=[validate_choice])

    class Meta:
        db_table = "ANSWER"
        unique_together = (("question_id", "assingment_id"), )


class CreatedQuiz:
    first_name = None
    last_name = None
    quiz_name = None
    start_date = None
    end_date = None

    def __init__(self, name, surname, qname, start, end):
        self.first_name = name
        self.last_name = surname
        self.quiz_name = qname
        self.start_date = start
        self.end_date = end

    def __str__(self):
        return "Organizer : " + self.first_name + " " + self.last_name + " Exam Name : " + self.quiz_name + " Start Time : " + self.start_date.__str__(
        ) + " End Date : " + self.end_date.__str__()


class AssignedQuiz:
    org_name = None
    quiz_name = None
    start_date = None
    end_date = None
    status = None

    def __init__(self, name, surname, qname, start, end):
        self.org_name = name + " " + surname
        utc = pytz.UTC
        self.quiz_name = qname
        self.start_date = start
        self.end_date = end
        now = utc.localize(dt.datetime.now())
        if start > now:
            self.status = 0
        elif start < now and end > now:
            self.status = 1
        else:
            self.status = 0
