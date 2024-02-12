from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .models import Task


class TaskCreationTestCase(APITestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(email="test_normal@user.com", password="foo")
        

    def test_task_creation(self):
    
        token = AccessToken.for_user(self.user)
        
        task_data = {
            'title': 'Tarea de prueba',
            'description': 'Esta es una tarea de prueba' 
        }

        headers = {'Authorization': f'Bearer {token}'}

        response = self.client.post(reverse('task-list'), task_data,headers=headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Task.objects.filter(title='Tarea de prueba').exists())

