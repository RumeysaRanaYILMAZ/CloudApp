from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField


# Create your models here.
class SysUser(AbstractUser):
    id = models.CharField(max_length=20, primary_key=True, db_column='id')
    saltkey = models.BinaryField(db_column='saltkey', null=False, default=b"")
    password = models.BinaryField(db_column='password',
                                  null=False,
                                  default=b"")
    date_joined = DateTimeField(db_column='date_joined', auto_now=True)
    is_organizer = models.BooleanField(db_column='is_organizer', default=False)

    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table = "SYSUSER"