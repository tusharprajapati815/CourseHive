from django.db import models
from App.models import Course
from tinymce.models import HTMLField

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to="review_avatars", null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = HTMLField(null=False)

    def __str__(self):
        return f'Review by {self.name} for {self.course.name}'