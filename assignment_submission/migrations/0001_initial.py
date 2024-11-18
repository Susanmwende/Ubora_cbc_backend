# Generated by Django 5.1.2 on 2024-10-31 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assignments', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('submission_id', models.AutoField(primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=10)),
                ('submitted_date', models.DateTimeField(auto_now_add=True)),
                ('completion_status', models.BooleanField(default=False)),
                ('image_upload', models.FileField(blank=True, upload_to='images/')),
                ('video_file', models.FileField(default='practical_videos/default_video.mp4', upload_to='practical_videos/')),
                ('assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.assignments')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
