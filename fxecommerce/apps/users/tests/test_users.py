import pytest


def test_new_user_model(django_user_model):
    user = django_user_model.objects.create(
        email="test@test.com",
        password="something",
        is_active=True,
        is_staff=True,
        is_superuser=True
    )

    assert user.email == 'test@test.com'
    assert user.password == 'something'
    assert user.is_active == True
    assert user.is_staff == True
    assert user.is_superuser == True
