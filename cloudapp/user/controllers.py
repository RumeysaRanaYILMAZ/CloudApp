from main.utils import Entity, IDGenerator
from exam.models import Exam
from .models import User
from cryptography.fernet import Fernet
from django.shortcuts import get_object_or_404


class OrganizerController:
    organizer = None

    def __init__(self, email):
        self.organizer = User.objects.filter(mail=email,
                                             is_organizer=True).get()

    def create_exam(self, name, start, end):
        examid = IDGenerator.generate(Entity.Exam)
        new_exam = Exam(id=examid,
                        name=name,
                        organizer=self.organizer,
                        start_time=start,
                        end_time=end)
        new_exam.save()
        return new_exam


class UserController:
    @staticmethod
    def user_add(password, email, first_name, last_name, isorganizer):
        userid = IDGenerator.generate(Entity.User)
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        hashpass = cipher_suite.encrypt(password.encode('utf-8'))
        User.objects.update_or_create(id=userid,
                                      password=hashpass,
                                      saltkey=key,
                                      name=first_name,
                                      surname=last_name,
                                      mail=email,
                                      is_organizer=isorganizer)

    @staticmethod
    def login(email, password):
        loguser = get_object_or_404(User, mail=email)
        cipher_suite = Fernet(loguser.key)
        if password == cipher_suite.decrypt(loguser.hashpass).decode('utf-8'):
            return loguser
        else:
            return None
