from django.db import models



class School(models.Model):
    code = models.CharField(max_length=100)
    school_name = models.CharField(max_length=255)
    level = models.CharField(max_length=100)
    school_status = models.CharField(max_length=100)
    school_type = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name
