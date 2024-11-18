
from django.db import models
from django.utils import timezone
from practical_activities.models import PracticalActivities

# Create your models here.

class Assignments(models.Model):
    assignment_id = models.AutoField(primary_key = True)
    practical_title = models.CharField(max_length = 50)
    description = models.CharField(max_length=255, default='Default description')
    practical_activity_id = models.ForeignKey(PracticalActivities, on_delete = models.CASCADE)
    submission_date = models.DateTimeField(default=timezone.now) 
    grade_level = models.CharField(max_length=20, default='1')  # Specify a default value
    points = models.BigIntegerField()
    def __str__(self):
        return f"{self.title}"
