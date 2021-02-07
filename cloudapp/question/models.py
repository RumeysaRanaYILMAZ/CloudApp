from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from exam.models import Assignment, Exam


def validate_choice(value):
    if value > 4:
        raise ValidationError(
            ('Index %(value)s is not a choice'),
            params={'value': value},
        )


# Create your models here.
class Question(models.Model):
    id = CharField(max_length=20,
                   primary_key=True,
                   db_column='QUESTID',
                   auto_created=True)
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
