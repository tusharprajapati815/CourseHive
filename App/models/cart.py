from django.db import models
from App.models import Course, UserCourse
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Cart'

    def __str__(self):
        return self.course.name
