from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

class GroupRequiredMixin(UserPassesTestMixin):
    group_required = []

    def test_func(self):
        user = self.request.user
        user_group = user.groups.filter(name__in=self.group_required).exists()
        return user_group or user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "You do not have rights to access this page")
        return HttpResponseRedirect('/')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name__in=self.group_required).exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)