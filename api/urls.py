from django.urls import path
from .views import AssignmentSubmissionListView
from .views import AssignmentSubmissionDetailView
from .views import AssignmentSubmissionCountView
from .views import AssignmentsListView
from .views import AssignmentsDetailView
from .views import PracticalActivitiesListView
from .views import PracticalActivitiesDetailView
# from .views import StudentListView
# from .views import StudentDetailView
# from .views import TeacherListView
# from .views import TeacherDetailView
from .views import UserListView
from .views import UserDetailView
from .views import QuestionAnswerListView
from .views import QuestionAnswerDetailView
from .views import QuestionAnswerThreadView
urlpatterns = [
    
    path('assignment-submission/', AssignmentSubmissionListView.as_view(), name='assignment_submission_list_view'),
    path('assignment-submission/<int:id>/', AssignmentSubmissionDetailView.as_view(), name='assignment_submission_detail_view'),
    path('assignments/count/', AssignmentSubmissionCountView.as_view(), name='assignment-submission-count'),


    
    path('assignments/', AssignmentsListView.as_view(), name='assignments_list_view'),
    path('assignments/<int:id>/', AssignmentsDetailView.as_view(), name='assignments_detail_view'),
    
    path('practical-activities/', PracticalActivitiesListView.as_view(), name='practical_activities_list_view'),
    path('practical-activities/<int:id>/', PracticalActivitiesDetailView.as_view(), name='practical_activities_detail_view'),
        
    # path('student/', StudentListView.as_view(), name='students_list_view'),
    # path('student/<int:id>/', StudentDetailView.as_view(), name='student_detail_view'),
    

    # path('teachers/', TeacherListView.as_view(), name='teachers_detalist'),
    # path('teachers/<int:id>/', TeacherDetailView.as_view(), name='teacher_detail'),

    path('users/', UserListView.as_view(), name='user-list'),
    
    path('users/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),

    path('questions/', QuestionAnswerListView.as_view(), name='question_list'),
    path('questions/<int:id>/', QuestionAnswerDetailView.as_view(), name='question_detail'),
    path('questions/<int:parent_id>/replies/', QuestionAnswerThreadView.as_view(), name='question_replies'),

]
