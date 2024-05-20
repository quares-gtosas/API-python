from rest_framework import serializers
from .models import Task, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'email']

class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='owner', write_only=True
    )

    class Meta:
        model = Task
        fields = ['id', 'owner', 'owner_id', 'task_desc', 'task_title', 'estimation_hour']