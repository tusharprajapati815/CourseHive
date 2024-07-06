from django.db import models
from tinymce.models import HTMLField
import bleach

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50, null=False)
    slug = models.CharField(max_length=50, null=False, unique=True)
    description = HTMLField( null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False , default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    resources = models.FileField(upload_to="resources")
    duration = models.IntegerField(null=False)

    class Meta:
        db_table = 'Course'

    def __str__(self):
        return self.name

class CourseProperty(models.Model):
    desc = HTMLField(null=False)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass

    class Meta:
        db_table = 'Tag'

class Requirements(CourseProperty):
    pass

    class Meta:
        db_table = 'Requirements'

class Learning(CourseProperty):
    pass

    class Meta:
        db_table = 'Learning'

