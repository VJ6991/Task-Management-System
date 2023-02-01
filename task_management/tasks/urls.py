from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tasks', TaskCreateView)

urlpatterns = [
    path('tasks/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks_comp/<int:pk>/', CompletedUsersListView.as_view(), name='task-completed'),
    path('tasks_sorted/<int:pk>/', SortedUsersListView.as_view(), name='task-sorted'),
    

]