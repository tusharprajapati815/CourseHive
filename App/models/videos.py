from django.db import models
from App.models import Course
from tinymce.models import HTMLField

class Videos(models.Model):
    title = models.CharField(max_length=100, null=False)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    serial_no = models.IntegerField(null=False)
    video_id = models.CharField(max_length=100, null=False)
    is_preview = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'Videos'
            
    def __str__(self):
        return self.title