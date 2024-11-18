# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from assignment_submission.models import AssignmentSubmission
from assignments.models import Assignments
from practical_activities.models import PracticalActivities
# from student.models import Student
# from teacher.models import Teacher
from user.models import User
from conversation.models import QuestionAnswer
from .serializers import (
    AssignmentSubmissionSerializer,
    AssignmentsSerializer,
    PracticalActivitiesSerializer,
    # StudentSerializer,
    # TeacherSerializer,
    UserSerializer,
    QuestionAnswerSerializer,

)

class QuestionAnswerListView(APIView):
    def get(self, request):
        # Retrieve all top-level questions (i.e., parent is null)
        questions = QuestionAnswer.objects.filter(parent=None)
        serializer = QuestionAnswerSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionAnswerDetailView(APIView):
    def get(self, request, id):
        try:
            question = QuestionAnswer.objects.get(id=id)
            serializer = QuestionAnswerSerializer(question)
            return Response(serializer.data)
        except QuestionAnswer.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            question = QuestionAnswer.objects.get(id=id)
            serializer = QuestionAnswerSerializer(question, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except QuestionAnswer.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            question = QuestionAnswer.objects.get(id=id)
            question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except QuestionAnswer.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

class QuestionAnswerThreadView(APIView):
    def get(self, request, parent_id):
        # Retrieve all follow-up answers for a specific parent question
        threads = QuestionAnswer.objects.filter(parent_id=parent_id)
        serializer = QuestionAnswerSerializer(threads, many=True)
        return Response(serializer.data)

class AssignmentSubmissionListView(APIView):
    def get(self, request):
        submissions = AssignmenSubmission.objects.all()
        serializer = AssignmentSubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignmentSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AssignmentSubmissionCountView(APIView):
    def get(self, request):
        # Get count of completed and not completed assignments
        counts = AssignmentSubmission.objects.count_completion_status()
        return Response(counts, status=status.HTTP_200_OK)

class AssignmentSubmissionDetailView(APIView):
    def get(self, request, id):
        submission = AssignmentSubmission.objects.get(id=id)
        serializer = AssignmentSubmissionSerializer(submission)
        return Response(serializer.data)

    def put(self, request, id):
        submission = AssignmentSubmission.objects.get(id=id)
        serializer = AssignmentSubmissionSerializer(submission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        submission = AssignmentSubmission.objects.get(id=id)
        submission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AssignmentsListView(APIView):
    def get(self, request):
        assignments = Assignments.objects.all()
        serializer = AssignmentsSerializer(assignments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignmentsDetailView(APIView):
    def get(self, request, id):
        assignment = Assignments.objects.get(id=id)
        serializer = AssignmentsSerializer(assignment)
        return Response(serializer.data)

    def put(self, request, id):
        assignment = Assignments.objects.get(id=id)
        serializer = AssignmentsSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        assignment = Assignments.objects.get(id=id)
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PracticalActivitiesListView(APIView):
    def get(self, request):
        activities = PracticalActivities.objects.all()
        serializer = PracticalActivitiesSerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PracticalActivitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PracticalActivitiesDetailView(APIView):
    def get(self, request, id):
        activity = PracticalActivities.objects.get(id=id)
        serializer = PracticalActivitiesSerializer(activity)
        return Response(serializer.data)

    def put(self, request, id):
        activity = PracticalActivities.objects.get(id=id)
        serializer = PracticalActivitiesSerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request,id): 
      activity=PracticalActivities.objects.get(id=id) 
      activity.delete() 
      return Response(status=HTTP.status.no_content) 


# class StudentListView(APIView):
#     def get(self, request):
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDetailView(APIView):
#     def get(self, request, id):
#         student= Student.objects.get(id=id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     def put(self, request, id):
#         student= Student.objects.get(id=id)
#         serializer = StudentSerializer(practical, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#     def delete(self, request,id): 
#       student=Student.objects.get(id=id) 
#       student.delete() 
#       return Response(status=HTTP.status.no_content) 


# class TeacherListView(APIView):
#     def get(self, request):
#         teacher = Teacher.objects.all()
#         serializer = TeacherSerializer(teacher, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TeacherSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TeacherDetailView(APIView):
#     def get(self, request, id):
#         teacher = Teacher.objects.get(id=id)
#         serializer = TeacherSerializer(teacher)
#         return Response(serializer.data)

#     def put(self, request, id):
#         teacher= Teacher.objects.get(id=id)
#         serializer = TeacherSerializer(teacher, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#     def delete(self, request,id): 
#       teacher= Teacher.objects.get(id=id) 
#       teacher.delete() 
#       return Response(status=HTTP.status.no_content)       





class TeacherAnswerListView(APIView):
    def get(self, request):
        teacherAnswer = TeacherAnswer.objects.all()
        serializer = TeacherAnswerSerializer(teacherAnswer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherAnswerDetailView(APIView):
    def get(self, request, id):
        teacherAnswer = TeacherAnswer.objects.get(id=id)
        serializer = TeacherAnswerSerializer(teacherAswer)
        return Response(serializer.data)

    def put(self, request, id):
        teacherAnswer= TeacherAnswer.objects.get(id=id)
        serializer = TeacherAnswerSerializer(teacherAswer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request,id): 
      teacherAswer= TeacherAnswer.objects.get(id=id) 
      teacherAswer.delete() 
      return Response(status=HTTP.status.no_content)       

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(user_id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id):
        try:
            user = User.objects.get(user_id=user_id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, user_id):
        try:
            user = User.objects.get(user_id=user_id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
