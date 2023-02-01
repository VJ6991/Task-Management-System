from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import *
from .serializers import TaskSerializer,UserSerializer
import datetime

class TaskCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        assigned_to = User.objects.get(id=self.request.data.get('assigned_to'))
        if Task.objects.filter(assigned_to=assigned_to,
                               created_at__date=datetime.datetime.today().date()).count() < 3:
            serializer.save(assigned_to=assigned_to)
        else:
            raise Exception("Maximum task limit for a user in a day reached")

class TaskUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class CompletedUsersListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        completed_tasks = Task.objects.filter(status=2)
        user_ids = []
        for task in completed_tasks:
            user_ids.append(task.assigned_to.id)
        user_ids = set(user_ids)
        users = User.objects.filter(id__in=user_ids)
        return users
        
class SortedUsersListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        completed_tasks = Task.objects.filter(status=2)
        user_task_count = {}
        for task in completed_tasks:
            if task.assigned_to.id in user_task_count:
                user_task_count[task.assigned_to.id] += 1
           