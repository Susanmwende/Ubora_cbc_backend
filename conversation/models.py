from django.db import models
from user.models import User

class QuestionAnswer(models.Model):
    question_id = models.AutoField(primary_key=True)
    content = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_questions')
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='follow_up')
    subject = models.CharField(max_length=30)
    is_question = models.BooleanField(default=True)  # Distinguish question vs. answer
    submitted_date = models.DateTimeField(auto_now_add=True)

    
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    
    def __str__(self):
        return f"{self.content} ({self.status})"
