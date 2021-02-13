from django.db import models


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True, db_column='id')
    saltkey = models.BinaryField(db_column='SALTKEY', null=False, default=b"")
    password = models.BinaryField(db_column='PASSWORD',
                                  null=False,
                                  default=b"")
    name = models.CharField(max_length=30,
                            null=False,
                            default="",
                            db_column='NAME')
    surname = models.CharField(max_length=50,
                               null=False,
                               default="",
                               db_column='SURNAME')
    mail = models.EmailField(db_column='EMAIL')
    is_organizer = models.BooleanField(db_column='ISORGANIZER', default=False)

    def __str__(self) -> str:
        return self.name + " " + self.surname

    class Meta:
        db_table = "USER"