import logging
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer


logger = logging.getLogger("todos")


class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        todo = serializer.save()
        logger.info(f"Todo created: {todo.title} (ID: {todo.id})")

    def perform_update(self, serializer):
        todo = serializer.save()
        logger.info(f"Todo updated: {todo.title} (ID: {todo.id})")

    def perform_destroy(self, instance):
        logger.info(f"Todo deleted: {instance.title} (ID: {instance.id})")
        instance.delete()