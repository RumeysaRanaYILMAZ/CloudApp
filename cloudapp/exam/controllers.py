from cloudapp.utils import Entity, IDGenerator
from user.models import SysUser
from exam.models import Assignment, Exam
from question.models import Answer, Question


class ExamController:
    questset = []
    exam = None

    def __init__(self, examid=None):
        if examid is not None:
            self.exam = Exam.objects.filter(pk=examid).get()
            self.questset = Question.objects.filter(exam_id=examid)

    def question_add(self, question):
        question.save()

    def question_add(self, contxt, ch1, ch2, ch3, ch4, corr):
        questid = IDGenerator.generate(Entity.Question)
        Question(id=questid,
                 exam_id=self.exam.id,
                 context=contxt,
                 choice1=ch1,
                 choice1=ch2,
                 choice1=ch3,
                 choice1=ch4,
                 correct=corr).save()

    def assign(self, usname):
        assignid = IDGenerator.generate(Entity.Assignment)
        Assignment(id=assignid, exam_id=self.exam.id, username=usname)

    def result_calculate(self, usname):
        results = {"correct": 0, "wrong": 0}
        assignment = Assignment.objects.filter(username=usname,
                                               exam_id=self.exam.id).get()
        answers = Answer.object.filter(assignment_id=assignment.id)

        for answer in answers:
            quest = Question.objects.filter(pk=answer.question_id).get()
            if quest.correct == answer.answer:
                results["correct"] += 1
            else:
                results["wrong"] += 1
        return results

    def show_assigned_exams(self, usname):
        return Assignment.objects.filter(username=usname)