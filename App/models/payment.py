from django.db import models
from App.models import UserCourse, Course
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Payment(models.Model):
    order_id = models.CharField(max_length=50, null=False)
    payment_id = models.CharField(max_length=50, null=True)
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)  #if status is failed there will be no data in user_course, it only take data entry when the payment is successful


    class Meta:
        db_table = 'Payment'