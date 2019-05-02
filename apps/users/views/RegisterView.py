from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.views import View

from apps.users.models import PingUser
from apps.utils.sendemail import send_register_email
from nova_collection.conf import body


class RegisterView(View):
    # def get(self, request):
    #     register_form = RegisterForm()
    #     return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        data = request.POST
        # register_form = RegisterForm(request.POST)
        # if register_form.is_valid():
        user_name = request.POST.get('email', '')
        if PingUser.objects.filter(email=user_name):
            body['code'] = 500
            body['status'] = 'fail'
            body['msg'] = '帐号已存在'
            return HttpResponse(body)
        pass_word = data.get('password')
        user_profile = PingUser()
        user_profile.username = user_name
        user_profile.email = user_name
        user_profile.is_active = False
        user_profile.password = make_password(pass_word)
        user_profile.save()
        send_register_email(user_name)
        body['code'] = 200
        body['status'] = 'success'
        body['msg'] = '注册成功'
        return HttpResponse(body)