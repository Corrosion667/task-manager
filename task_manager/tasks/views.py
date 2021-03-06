"""Module with views logic of the tasks app."""

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from task_manager.custom_views import CustomLoginMixin
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.models import Task


class TasksListView(CustomLoginMixin, FilterView):
    """View for tasks page."""

    template_name = 'tasks.html'
    context_object_name = 'tasks_list'
    filterset_class = TaskFilter


class CreateTaskView(SuccessMessageMixin, CustomLoginMixin, CreateView):
    """View for create task page."""

    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'create_task.html'
    success_message = _('Task successfully created')
    fields = [
        'name',
        'description',
        'status',
        'executor',
        'labels',
    ]

    def form_valid(self, form):
        """Set author of task as active user."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(SuccessMessageMixin, CustomLoginMixin, UpdateView):
    """View for change task data page."""

    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully changed')
    template_name = 'update_task.html'
    fields = [
        'name',
        'description',
        'status',
        'executor',
        'labels',
    ]


class DeleteTaskView(SuccessMessageMixin, CustomLoginMixin, DeleteView):
    """View for task deletion page."""

    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')
    unable_to_delete_others_tasks = _(
        'Task can only be deleted by its author',
    )

    def get(self, request, *args, **kwargs):
        """GET requests method.

        Returns:
            Execute GET request or redirect if user tries to delete not his own task.
        """
        if request.user != self.get_object().author:
            messages.error(
                self.request, self.unable_to_delete_others_tasks,
            )
            return redirect('tasks')
        return super().get(request, *args, **kwargs)


class TaskDetailsView(CustomLoginMixin, DetailView):
    """View for page with task details."""

    model = Task
    template_name = 'task_details.html'
