from exam.models import Assignment
from .models import Answer


class AnswerController:
    @staticmethod
    def answer(question, usname, ansnumber):
        assignment = Assignment.objects.filter(username=usname,
                                               exam_id=question.exam_id)
        Answer(question_id=question.id,
               assignment_id=assignment.id,
               answer=ansnumber)
