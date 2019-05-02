from django.http import JsonResponse
from django.views import View

from apps.utils.Authentication import auth_permission_required


class TestView(View):
    @auth_permission_required('apps.users')
    def get(self, request):
        # _jsondata = {
        #     "user": "yerikyu",
        #     "site": "treestore@foxmail.com"
        # }
        body = '1'
        return JsonResponse({"state": 1, "message": body})
