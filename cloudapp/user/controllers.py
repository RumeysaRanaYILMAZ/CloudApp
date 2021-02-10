from cloudapp.utils import Entity, IDGenerator
from exam.models import Exam
from .models import SysUser
from cryptography.fernet import Fernet
from django.shortcuts import get_object_or_404


class OrganizerController:
    organizer = None

    def __init__(self, usname):
        self.organizer = SysUser.objects.filter(username=usname,
                                                is_organizer=True)

    def create_exam(self, name, start, end):
        examid = IDGenerator.generate(Entity.Exam)
        Exam(id=examid,
             name=name,
             organizer=self.organizer,
             start_time=start,
             end_time=end)


class UserController:
    @staticmethod
    def user_add(username, password, mail, name, surname, isorganizer):
        userid = IDGenerator.generate(Entity.SysUser)
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        hashpass = cipher_suite.encrypt(password.encode('utf-8'))
        SysUser.objects.update_or_create(id=userid,
                                         password=hashpass,
                                         saltkey=key,
                                         is_superuser=False,
                                         username=username,
                                         first_name=name,
                                         last_name=surname,
                                         email=mail,
                                         is_staff=False,
                                         is_active=True,
                                         is_organizer=isorganizer)

    @staticmethod
    def login(usname, password):
        loguser = get_object_or_404(SysUser, username=usname)
        cipher_suite = Fernet(loguser.key)
        if password == cipher_suite.decrypt(loguser.hashpass).decode('utf-8'):
            return True
        else:
            return False
