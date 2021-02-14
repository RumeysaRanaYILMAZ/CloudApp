from question.controllers import QuestionController
from main.utils import Entity, IDGenerator
from exam.models import Assignment, Exam
from exam.examview import ExamView
from question.models import Answer, AssignedQuiz, Question, CreatedQuiz
from user.models import User


class ExamController:
    questset = []
    exam = None

    def __init__(self, examid=None):
        if examid is not None:
            self.exam = Exam.objects.filter(pk=examid).get()
            self.questset = Question.objects.filter(exam_id=examid)

    @staticmethod
    def exam_update(Exam_View):
        selected = Exam.objects.filter(pk=Exam_View.id).get()
        selected.name = Exam_View.name
        selected.start_time = Exam_View.start
        selected.end_time = Exam_View.end
        selected.save()
        for question in Exam_View.questions:
            questcon = QuestionController(question.id)
            questcon.question_update(question.context, question.choice1,
                                     question.choice2, question.choice3,
                                     question.choice4, question.correct)

    def exam_show(self):
        return ExamView(self.exam.id)

    def question_add(self, contxt, ch1, ch2, ch3, ch4, corr):
        questid = IDGenerator.generate(Entity.Question)
        Question(id=questid,
                 exam_id=self.exam,
                 context=contxt,
                 choice1=ch1,
                 choice2=ch2,
                 choice3=ch3,
                 choice4=ch4,
                 correct=corr).save()

    def assign(self, userid):
        assignid = IDGenerator.generate(Entity.Assignment)
        user = User.objects.filter(id=userid).get()
        Assignment(id=assignid, exam_id=self.exam, user_id=user).save()

    def result_calculate(self, email):
        results = {"correct": 0, "wrong": 0}
        user = User.objects.filter(mail=email).get()
        assignment = Assignment.objects.filter(user_id=user.id,
                                               exam_id=self.exam.id).get()
        answers = Answer.object.filter(assignment_id=assignment.id)

        for answer in answers:
            quest = Question.objects.filter(pk=answer.question_id).get()
            if quest.correct == answer.answer:
                results["correct"] += 1
            else:
                results["wrong"] += 1
        return results

    @staticmethod
    def show_assigned_exams(email):
        user = User.objects.filter(mail=email).get()
        assignments = Assignment.objects.filter(
            user_id=user.id).prefetch_related('user_id', 'exam_id')
        examlist = []
        for assign in assignments:
            examlist.append(
                AssignedQuiz(assign.exam_id.id, assign.exam_id.organizer.name,
                             assign.exam_id.organizer.surname,
                             assign.exam_id.name, assign.exam_id.start_time,
                             assign.exam_id.end_time))
        return examlist

    @staticmethod
    def show_created_exams(email):
        examlist = []
        try:
            user = User.objects.filter(mail=email, is_organizer=True).get()
            exams = Exam.objects.filter(
                organizer=user.id).prefetch_related('organizer')
            for exam in exams:
                examlist.append(
                    CreatedQuiz(exam.id, exam.organizer.name,
                                exam.organizer.surname, exam.name,
                                exam.start_time, exam.end_time))
        except Exception:
            print("Uygun User bulunamadı")

        return examlist

    def examscores(self):
        return Assignment.objects.filter(
            exam_id=self.exam.id).order_by('result').reverse()
