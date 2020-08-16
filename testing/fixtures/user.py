from django.contrib.auth.models import User

import pytest
from rest_framework.authtoken.models import Token

@pytest.fixture
def user(request):
    user = User(email='user@test.com', username='test_user')
    user.set_password('test1231234')
    user.save()
    return user


@pytest.fixture
def admin_user(request):
    user = User(email='admin@test.com', username='admin_user')
    user.set_password('test1231234')
    user.is_superuser = True
    user.save()
    return user