from rest_framework import serializers
from .models import Task,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'id', 'phone_number')

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'assigned_to')