from django.http import JsonResponse
from django.views import View

from apps.users.models import EmailVerifyRecord, PingUser


# 验证用户注册后，在邮件里点击注册链接
class CheckUrlView(View):
    def get(self, request, active_code):
        # 为什么用 filter ？ 因为用户可能注册了好多次，一个 email 对应了好多个 code
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for records in all_records:
                email = records.email
                user = PingUser.objects.get(email=email)
                user.is_active = True
                user.save()
                body = {'code': 200, 'status': 'success', 'msg': 'activity'}
        else:
            body = {'code': 500, 'status': 'fail', 'msg': 'inactive'}
        return JsonResponse(body)
