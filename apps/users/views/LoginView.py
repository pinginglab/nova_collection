from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from django.views import View

from nova_collection.conf import body


class LoginView(View):
    # def get(self, request):
    #     return render(request, 'login.html', {})

    def post(self, request):
        data = request.POST
        # login_form = LoginForm(request.POST)
        # if login_form.is_valid():
        user_name = data.get('username', '')
        password = data.get('password', '')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                body['code'] = 200
                body['status'] = 'success'
                body['msg'] = ''
                return HttpResponse(body)
            else:
                return HttpResponse(request, 'login.html', {'msg': '用户未激活！'})
        else:
            return HttpResponse(request, 'login.html', {'msg': '用户名或者密码错误！'})
