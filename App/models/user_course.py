from django.db import models
from App.models import Course
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class UserCourse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.name}'
    
    class Meta:
        db_table = 'Usercourse'