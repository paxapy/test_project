from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings

from factories import UserFactory

class ProfileTest(TestCase):

    def test_creating_profile(self):
        self.user = UserFactory.create()
        self.assertEquals(self.user, self.user.profile.user)

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

class ContextSettingsTest(TestCase):
    def test_settings_in_context(self):
        login_url = reverse('login')
        response = self.client.get(login_url)
        self.assertEquals(response.context['settings'].PROJECT_NAME, settings.PROJECT_NAME)