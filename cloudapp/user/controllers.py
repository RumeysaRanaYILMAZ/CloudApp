from exam.models import Exam
from .models import SysUser


class OrganizerController:
    organizer = None

    def __init__(self, usname):
        self.organizer = SysUser.objects.filter(username=usname,
                                                is_organizer=True)

    def create_exam(self, name, start, end):
        Exam(name=name,
             organizer=self.organizer,
             start_time=start,
             end_time=end)
