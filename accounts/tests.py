from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings

from accounts.factories import ProfileFactory, USER_PASSWORD
from accounts.models import Profile


class AuthenticationTest(TestCase):

    def setUp(self):
        self.user = ProfileFactory()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

    def test_login(self):
        response = self.client.post(
            self.login_url,
            {'username': self.user.username, 'password': USER_PASSWORD}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['_auth_user_id'], self.user.pk)

    def test_logout(self):
        self.client.login(username=self.user.username, password=USER_PASSWORD)
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get('_auth_user_id'), None)


class ProfileTest(TestCase):

    def setUp(self):
        self.profile = ProfileFactory()
        self.client.login(username=self.profile.username, password=USER_PASSWORD)

    def test_profile_details(self):
        response = self.client.get(reverse('profile_detail'))
        self.assertEqual(response.status_code, 200)
        context_obj = response.context['object']
        self.assertEqual(context_obj.first_name, self.profile.first_name)
        self.assertEqual(context_obj.last_name, self.profile.last_name)
        self.assertEqual(context_obj.birthday, self.profile.birthday)
        self.assertEqual(context_obj.biography, self.profile.biography)
        self.assertEqual(context_obj.contacts, self.profile.contacts)

    def test_profile_update(self):
        profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(profile.first_name, 'John')
        response = self.client.post(reverse('profile_update'), {'first_name': 'Mike', })
        self.assertEqual(response.status_code, 302)
        profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(profile.first_name, 'Mike')

    def test_profile_details_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('profile_detail'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response['location'])

    def test_profile_update_unauthenticated(self):
        self.client.logout()
        profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(profile.first_name, 'John')
        response = self.client.post(reverse('profile_update'), {'first_name': 'Mike', })
        self.assertEqual(response.status_code, 302)
        profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(profile.first_name, 'John')
        self.assertIn(reverse('login'), response['location'])


class ContextSettingsTest(TestCase):

    def test_settings_in_context(self):
        login_url = reverse('login')
        response = self.client.get(login_url)
        self.assertEqual(response.context['settings'].PROJECT_NAME, settings.PROJECT_NAME)
