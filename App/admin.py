from django.contrib import admin
from App.models import Course, Tag, Requirements, Learning, Videos, Course, UserCourse, Payment, Cart, Review

# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag
    
class RequirementsAdmin(admin.TabularInline):
    model = Requirements

class LearningAdmin(admin.TabularInline):
    model = Learning

class VideoAdmin(admin.TabularInline):
    model = Videos

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, RequirementsAdmin, LearningAdmin, VideoAdmin]

class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'course']

admin.site.register(Course, CourseAdmin)

admin.site.register(Videos)

admin.site.register(Payment)

admin.site.register(UserCourse)

admin.site.register(Cart, CartAdmin)

admin.site.register(Review)
