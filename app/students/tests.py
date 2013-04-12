"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test.client import Client
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from app.groups.models import Group
from app.students.models import Student

import os

class SimpleTest(TestCase):
    group_stub = {'name': 'test_group'}
    user_stub = {'first_name': 'test', 'last_name': 'user', 
                 'birthday': '2013-01-05', 'uid': '12346', 
                 'photo': os.path.dirname(__file__) + '/fixtures/photo.jpg'}
    
    def setUp(self):
        self.user = User.objects.create_user('sm', 'sm@mail.com', '123456')
        
        
        
    def tearDown(self):
        self.user.delete()
        
    def login(self):
        self.client.login(username='sm', password='123456')
    
    def test_home_page(self):
        self.login()

        # add new group
        self.client.post(reverse('group_add'), self.group_stub, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        groups = Group.objects.filter(name=self.group_stub['name'])
        self.assertEqual(groups.count(), 1)

        # add new student
        with open(self.user_stub['photo']) as fp:
            self.user_stub['photo'] = fp
            self.client.post(reverse('student_add', args=(groups[0].id,)), self.user_stub, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        students = Student.objects.filter(group=groups[0])
        self.assertEqual(students.count(), 1)
