import datetime
from enum import Enum
from user.models import User
from exam.models import Exam, Assignment
from question.models import Question, Answer


class Entity(Enum):
    User = 1
    Exam = 2
    Assignment = 3
    Question = 4
    Answer = 5


class IDGenerator:
    @staticmethod
    def generate(servis):
        idcode = ''
        lastid = ""
        try:
            if servis == Entity.User:
                idcode = 'USR'
                last_object = User.objects.all().order_by('id').last()
                lastid = last_object.id
            elif servis == Entity.Exam:
                idcode = 'EXM'
                last_object = Exam.objects.all().order_by('id').last()
                lastid = last_object.id
            elif servis == Entity.Assignment:
                idcode = 'ASG'
                last_object = Assignment.objects.all().order_by('id').last()
                lastid = last_object.id
            elif servis == Entity.Question:
                idcode = 'QST'
                last_object = Question.objects.all().order_by('id').last()
                lastid = last_object.id
            elif servis == Entity.Answer:
                idcode = 'ANS'
                last_object = Answer.objects.all().order_by('id').last()
                lastid = last_object.id
            return IDGenerator.generatenumber(idcode, lastid)
        except Exception as e:
            print(e)
            return IDGenerator.generatefirst(idcode)

    @staticmethod
    def generatenumber(idcode, lastid):
        obj_int = int(lastid[9:13])
        new_message_int = obj_int + 1
        new_id = idcode + str(str(datetime.date.today().year)) + str(
            datetime.date.today().month).zfill(2) + str(new_message_int).zfill(
                4)
        return new_id

    @staticmethod
    def generatefirst(idcode):
        return idcode + str(datetime.date.today().year) + str(
            datetime.date.today().month).zfill(2) + '0000'
