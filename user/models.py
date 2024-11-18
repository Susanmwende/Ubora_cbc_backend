from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20, default="unknown")
    password = models.CharField(max_length=128, default='default_password')
    school_name=models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    
    TEACHER = 'teacher'
    STUDENT = 'student'
    ROLE_CHOICES = [
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    ]

    # Define the role field using choices
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=STUDENT,  # Default to student
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
