from django.db import models
from user.models import User
from django.utils.timezone import now


class PracticalActivities(models.Model):
    practical_activity_id = models.AutoField(primary_key=True)
    practical_name = models.CharField(max_length=100, default='Practical')  # Set a default value
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    grade_level = models.CharField(max_length=20, default='1')  # Specify a default value
    duration = models.DurationField()
    instruction = models.TextField()
    submission_date = models.DateTimeField(default=now)
    video_file = models.FileField(upload_to='practical_videos/', default='practical_videos/default_video.mp4')  # Set a default value
    def __str__(self):
        return f"{self.activity_name}"

   




































































   