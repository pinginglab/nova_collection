import hashlib
import uuid

from django.core.mail import send_mail
from django.http import HttpResponse

from apps.users.models import EmailVerifyRecord
from nova_collection.conf import body
from nova_collection.conf.email import DEFAULT_FROM_EMAIL


def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = get_random_str()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    url = "http://127.0.0.1:8000/user/active/"+code
    email_record.save()
    # 保存到数据库完成
    send_my_email(url, email)


def send_my_email(req, rec):
    title = "pingsec攻防平台注册码"
    email_from = DEFAULT_FROM_EMAIL
    try:
        # 发送邮件
        send_mail(title, req, email_from, rec)
    except Exception as e:
        body['code'] = 500
        body['status'] = 'fail'
        body['msg'] = e
        return HttpResponse(body)
    body['code'] = 200
    body['status'] = 'success'
    body['msg'] = '已发送'
    return HttpResponse(body)
