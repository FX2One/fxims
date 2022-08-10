import pytest

@pytest.fixture
def create_admin(django_user_model):
    """return default admin user"""

    return django_user_model.objects.create_superuser("admin","admin@admin.com","password")