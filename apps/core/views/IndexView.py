from django.http import JsonResponse
from django.views import View


class IndexView(View):
    def get(self):
        body = {'code': 200, 'status': 'success', 'msg': 'index'}
        return JsonResponse(body)
