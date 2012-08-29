
from django.test import TestCase

from factories import UserFactory

class ProfileTest(TestCase):
    def test_creating_profile(self):
        user = UserFactory.create()
        self.assertEquals(user, user.profile.user)