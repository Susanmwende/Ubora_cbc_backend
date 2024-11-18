# urls.py
from django.urls import path
from .views import upload_school_csv

urlpatterns = [
    path('upload-school-csv/', upload_school_csv, name='upload_school_csv'),
]
