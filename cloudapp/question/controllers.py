from cloudapp.utils import Entity, IDGenerator
from exam.models import Assignment
from .models import Answer,Question
from exam.models import Exam


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

class QuestionController:

    @staticmethod
    def questions(examId):
        questions = Question.objects.filter(exam_id__question=examId)
        return questions