from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Todo


class TodoAPITests(APITestCase):

    def test_create_todo(self):
        url = "/api/todos/"

        data = {
            "title": "Test Todo",
            "description": "Testing API",
            "is_completed": False
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)

    def test_list_todos(self):
        Todo.objects.create(title="Todo 1", description="Desc")

        url = "/api/todos/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_todo(self):
        todo = Todo.objects.create(title="Single Todo")

        url = f"/api/todos/{todo.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo(self):
        todo = Todo.objects.create(title="Old")

        url = f"/api/todos/{todo.id}/"

        data = {
            "title": "New",
            "description": "",
            "is_completed": True
        }

        response = self.client.put(url, data)

        todo.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(todo.title, "New")

    def test_delete_todo(self):
        todo = Todo.objects.create(title="Delete me")

        url = f"/api/todos/{todo.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)

    def test_validation_error(self):
        url = "/api/todos/"

        data = {
            "title": "   ",
            "description": "Invalid"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)