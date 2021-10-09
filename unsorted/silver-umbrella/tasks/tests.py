import json
from datetime import datetime

import pytest
from django.test import TestCase
from django.utils import timezone

from tasks.models import Task

# fmt: off
task_list = json.loads("""[{"title":"Make dinner","group":"Scuba Divers","task":"Web project","created_by":"shacker","date_created":"","date_due":"2019-06-14","completed":false,"note":"Please check with mgmt first","priority":3},{"title":"Bake bread","group":"Scuba Divers","task":"Example List","created_by":"mr_random","date_created":"2012-03-14","date_due":"","completed":true},{"title":"Bring dessert","group":"Scuba Divers","task":"Web project","created_by":"user1","date_created":"2015-06-248","date_due":"","assigned_to":"user1","note":"Every generation throws a hero up the pop charts","priority":77},{"external_id":"5bc397e7-4cdc-4408-9ae8-1e1c86ca5a64","title":"computer sciences","content":"HTML I","date_modified":null,"date_created":"2021-07-02T21:52:08.292Z","date_due":null,"completed":true},{"external_id":"7b22aba3-db69-4359-8950-2a9c5a924a8c","title":"computer sciences","content":"CSS","date_modified":null,"date_created":"2021-07-02T21:52:08.292Z","date_due":null,"completed":true},{"external_id":"ca7be5a1-99e7-4950-8758-5ce926e0bc3c","title":"computer sciences","content":"Responsive design","date_modified":null,"date_created":"2021-07-02T21:52:08.292Z","date_due":null,"completed":true},{"external_id":"e5b42abe-69b4-4268-8cc7-a5c549945f8d","title":"computer sciences","content":"Git","date_modified":null,"date_created":"2021-07-02T21:52:08.292Z","date_due":null,"completed":true},{"external_id":"d81c8991-d82e-4c0e-a63e-83d8145a1912","title":"computer sciences","content":"JavaScript I","date_modified":null,"date_created":"2021-07-02T21:52:08.292Z","date_due":null,"completed":true},{"external_id":"c7d16094-4bcd-4dfe-b54f-91565a45c07a","title":"computer sciences","content":"JavaScript II","date_modified":null,"date_created":"2021-07-02T21:52:08.292Z","date_due":null,"completed":false}]""")
# fmt: on
from tasks.models import Task

today = timezone.now()
# https://devcenter.heroku.com/articles/heroku-redis#upgrading-a-heroku-redis-version
# Create your tests here.
# def test_versioning():
#     first_check = r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
#     second_check = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
#     assert True == True

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

    def test_task_10_title(self):
        assert self.task_10.title == "ITM304"

    def test_task_10_content(self):
        assert self.task_10.content == "Quiz 6 SQL, Database Redesign"

    def test_task_10_date_modified(self):
        assert self.task_10.date_modified == None

    def test_task_10_date_created(self):
        assert self.task_10.date_created == self.task_10.date_created

    def test_task_10_date_due(self):
        assert self.task_10.date_due == None

    def test_task_10_completed(self):
        assert self.task_10.completed == True
