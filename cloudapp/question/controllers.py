from cloudapp.utils import Entity, IDGenerator
from exam.models import Assignment
from .models import Answer


class AnswerController:
    @staticmethod
    def answer(question, usname, ansnumber):
        assignment = Assignment.objects.filter(username=usname,
                                               exam_id=question.exam_id)
        answerid = IDGenerator.generate(Entity.Answer)
        Answer(id=answerid,
               question_id=question.id,
               assignment_id=assignment.id,
               answer=ansnumber)
