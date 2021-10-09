import json
from datetime import date, timedelta

import pytest
from django.contrib.auth import get_user_model
from django.test import AsyncRequestFactory, Client, TestCase

from blog.models import Post
from blog.views import api_list_announcements

today = date.today()
tomorrow = today + timedelta(days=1)


class TestPost(TestCase):
    fixtures = ("datainit.json",)
    pytestmark = pytest.mark.django_db

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.shunsui = get_user_model().objects.get(username="shunsui_kyoraku")
        cls.unohana = get_user_model().objects.get(username="retsu_unohana")
        cls.zaraki = get_user_model().objects.get(username="kenpachi_zaraki")
        cls.first = Post.objects.get(pk=1)
        cls.second = Post.objects.get(pk=2)
        cls.third = Post.objects.get(pk=3)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_first_post_post_date_expired(self):
        """
        when "date_posted" is July 4, 2021
        tomorrow is July 5, 2021
        """
        self.first.date_expired = self.first.date_posted + timedelta(days=1)
        self.first.save()
        assert self.first.date_expired.year == 2021
        assert self.first.date_expired.month == 7
        assert self.first.date_expired.day == 5
