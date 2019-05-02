from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from django.views import View

from apps.users.models import PingUser


class LoginView(View):
    # def get(self, request):
    #     return render(request, 'login.html', {})

    def post(self, request):
        data = eval(request.body.decode())
        user_name = data.get('username', '')
        password = data.get('password', '')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                user = PingUser.objects.get(username=user_name)
                body = {'code': 200, 'status': 'success', 'msg': {'token': user.token}}
            else:
                body = {'code': 400, 'status': 'fail', 'msg': '用户未激活!'}
        else:
            body = {'code': 400, 'status': 'fail', 'msg': '用户名或者密码错误!'}
        return JsonResponse(body)
