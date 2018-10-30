from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 6:
            errors['course_name'] = "Course name should be at least 6 characters"
        if len(postData['desc']) < 16:
            errors['desc'] = "Description should be at least 16 characters"
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()