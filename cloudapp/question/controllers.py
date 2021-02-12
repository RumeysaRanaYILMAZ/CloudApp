from cloudapp.utils import Entity, IDGenerator
from exam.models import Assignment
from .models import Answer, Question
from user.models import User


class AnswerController:
    @staticmethod
    def answer(questid, email, ansnumber):
        user = User.objects.filter(mail=email).get()
        question = Question.objects.filter(pk=questid).get()
        assignment = Assignment.objects.filter(user_id=user.id,
                                               exam_id=question.exam_id)
        answerid = IDGenerator.generate(Entity.Answer)
        Answer(id=answerid,
               question_id=question.id,
               assignment_id=assignment.id,
               answer=ansnumber).save()
