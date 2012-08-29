from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from factories import UserFactory, ProfileFactory

class ProfileTest(TestCase):
    profile = ProfileFactory.stub()
    url = reverse('profile_detail')
    client = Client()
    response = client.get(url)
    response_obj = response.context['object']

    def test_creating_profile(self):
        user = UserFactory.create()
        self.assertEquals(user, user.profile.user)

    def test_profile_first_name(self):
        self.assertEquals(self.profile.first_name, self.response_obj.first_name)

    def test_profile_last_name(self):
        self.assertEquals(self.profile.last_name, self.response_obj.last_name)

    def test_profile_birthday(self):
        self.assertEquals(self.profile.birthday, self.response_obj.birthday)

    def test_profile_biography(self):
        self.assertEquals(self.profile.biography, self.response_obj.biography)

    def test_profile_contacts(self):
        self.assertEquals(self.profile.contacts, self.response_obj.contacts)

class AuthenticationTest(TestCase):
    user = UserFactory.build()
    login_url = reverse('login')
    logout_url = reverse('logout')

    def test_login(self):
        response = self.client.post(self.login_url,{'username':self.user.username, 'password':self.user.password})
        self.assertEquals(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)