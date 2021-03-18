from django.db import models
from django.contrib.auth.models import User
# from authemail.models import EmailUserManager, EmailAbstractUser


# Create your models here.
class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_phone = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.user.first_name
