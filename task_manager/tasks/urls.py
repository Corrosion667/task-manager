"""URL routing of the tasks app."""

from django.urls import path

from task_manager.tasks.views import (
    CreateTaskView,
    DeleteTaskView,
    TasksListView,
    UpdateTaskView,
)

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
]
