from .models import Exam
from question.models import Question


class ExamView:
    id = None
    name = None
    instructor = None
    questions = None
    start = None
    end = None

    def __init__(self, examid):
        self.id = examid
        selected_exam = Exam.objects.filter(id=examid).get()
        self.name = selected_exam.name
        self.instructor = selected_exam.organizer
        self.questions = Question.objects.filter(exam_id=examid)
        self.start = selected_exam.start_time
        self.end = selected_exam.end_time