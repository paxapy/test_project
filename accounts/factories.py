import factory
from datetime import date

from accounts.models import Profile


USER_PASSWORD = 'qwe'


class ProfileFactory(factory.Factory):
    FACTORY_FOR = Profile

    username = 'john_doe'
    password = USER_PASSWORD
    first_name = 'John'
    last_name = 'Doe'
    email = 'john.doe@gmail.com'

    birthday = date.today()
    biography = 'Some test bio'
    contacts = 'email: john.doe@gmail.com, phone: +1 234 567 89 01'

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        profile = super(ProfileFactory, cls)._prepare(create, **kwargs)
        if password:
            profile.set_password(password)
            if create:
                profile.save()
        return profile
