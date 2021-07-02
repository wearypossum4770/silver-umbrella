from datetime import datetime

import pytest
from django.test import TestCase
from django.utils import timezone

from tasks.models import Task


# https://devcenter.heroku.com/articles/heroku-redis#upgrading-a-heroku-redis-version
# Create your tests here.
class TestTasks(TestCase):
    fixtures = ("datainit.json",)
    pytestmark = pytest.mark.django_db
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.task_10 = Task.objects.get(pk=10)
        cls.tasks = Task.objects.all()
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
    def test_task_list_loaded(self):
        assert len(self.tasks) > 0
    def test_task_10_title (self):
        assert self.task_10.title == "ITM304"
    def test_task_10_content(self):
        assert self.task_10.content ==  "Quiz 6 SQL, Database Redesign"
    def test_task_10_date_modified(self):
        assert self.task_10.date_modified == None
    def test_task_10_date_created(self):
        assert self.task_10.date_created == self.task_10.date_created
    def test_task_10_date_due(self):
        assert self.task_10.date_due == None
    def test_task_10_completed(self):
        assert self.task_10.completed == True

# [
# {"task":"HTML I","done":true},
# {"task":"CSS","done":true},
# {"task":"Responsive design","done":true},
# {"task":"Git","done":true},
# {"task":"JavaScript I","done":true},
# {"task":"JavaScript II","done":false}
# ]
