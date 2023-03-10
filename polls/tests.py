from django.test import TestCase

import datetime
from django.utils import timezone

from .models import Question


class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pubdate=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):

        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        old_question = Question(pubdate=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):

        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        recent_question = Question(pubdate=time)
        self.assertIs(recent_question.was_published_recently(), True)
