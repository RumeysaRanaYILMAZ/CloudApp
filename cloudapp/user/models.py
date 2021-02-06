from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class SysUser(AbstractUser):
    is_organizer = models.BooleanField(db_column='ISORGANIZER', default=False)

    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table = "SYSUSER"