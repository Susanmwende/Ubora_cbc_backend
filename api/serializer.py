from rest_framework import serializers
from practical_activities.models import PracticalActivities
from assignment_submission.models import AssignmentSubmission
from assignments.models import Assignments
from user.models import User
from conversation.models import QuestionAnswer


class PracticalActivitiesSerializer(serializers.ModelSerializer):
      class Meta:
            model = PracticalActivities
            fields = "_all_"

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
      class Meta:
            model = AssignmentSubmission
            fields = "_all_"            


class AssignmentsSerializer(serializers.ModelSerializer):
      class Meta:
            model = Assignments
            fields = "_all_"  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = "__all__"
  