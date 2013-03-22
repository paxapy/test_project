
import factory
from datetime import date

from django.contrib.auth.models import User

from accounts.models import Profile


class UserFactory(factory.Factory):
    FACTORY_FOR = User
    username = 'John'
    password = 'test_user'


class ProfileFactory(factory.Factory):
    FACTORY_FOR = Profile
    first_name = 'John'
    last_name = 'Doe'
    birthday = date.today()
    biography = 'Some test bio'
    contacts = 'email: john.doe@gmail.com, phone: +1 234 567 89 01'
