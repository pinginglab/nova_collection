from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views import View

from apps.users.models import PingUser
from apps.utils.Sendemail import send_register_email


class RegisterView(View):
    # def get(self, request):
    #     register_form = RegisterForm()
    #     return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        data = eval(request.body.decode())
        user_name = data.get('email', '')
        if PingUser.objects.filter(email=user_name):
            body = {'code': 500, 'status': 'fail', 'msg': '帐号已存在:('}
            return JsonResponse(body)
        pass_word = data.get('password')
        user_profile = PingUser()
        user_profile.username = user_name
        user_profile.email = user_name
        user_profile.is_active = False
        user_profile.password = make_password(pass_word)
        try:
            user_profile.save()
            send_register_email(user_name)
            body = {'code': 200, 'status': 'success', 'msg': '注册成功\n请查看邮箱通过验证码激活:)'}
        except Exception as e:
            body = {'code': 400, 'status': 'fail', 'msg': e.__str__()}
        return JsonResponse(body)
