# Create your models here.
from django.db import models
from user.models import User
from assignments.models import Assignments

class AssignmentSubmissionManager(models.Manager):
    def count_completion_status(self):
        return {
            "completed": self.filter(completion_status=True).count(),
            "not_completed": self.filter(completion_status=False).count(),
        }

class AssignmentSubmission(models.Model):
    submission_id = models.AutoField(primary_key=True)  # Ensure this is the primary key
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    submitted_date = models.DateTimeField(auto_now_add=True)
    completion_status = models.BooleanField(default=False)
    image_upload = models.FileField(upload_to='images/', blank=True) 
    video_file = models.FileField(upload_to='practical_videos/', default='practical_videos/default_video.mp4')  # Set a default value


    # Add the custom manager
    objects = AssignmentSubmissionManager()

    def __str__(self):
        return f"Submission {self.submission_id} - Grade: {self.grade}"

    @classmethod
    def count_submissions(cls, assignment_id):
        """Count the number of submissions for a specific assignment."""
        return cls.objects.filter(assignment_id=assignment_id).count()


