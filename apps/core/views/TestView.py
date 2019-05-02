from django.views import View

from apps.utils.Authentication import auth_permission_required


class TestView(View):
    @auth_permission_required('apps.users.select_user')
    def get(self):
        pass