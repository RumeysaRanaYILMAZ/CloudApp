from main.utils import Entity, IDGenerator
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
               answer=ansnumber).save()


class QuestionController:
    question = None

    def __init__(self, questid):
        self.question = Question.objects.filter(pk=questid).get()

    def question_update(self, contxt, ch1, ch2, ch3, ch4, corr):
        Question(id=self.question.id,
                 exam_id=self.question.exam_id,
                 context=contxt,
                 choice1=ch1,
                 choice2=ch2,
                 choice3=ch3,
                 choice4=ch4,
                 correct=corr).save()
