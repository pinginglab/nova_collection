import hashlib
import uuid

from django.core.mail import send_mail
from django.http import HttpResponse

from apps.users.models import EmailVerifyRecord
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
    url = "点击连接完成激活:http://127.0.0.1:8000/account/active/" + code
    email_record.save()
    # 保存到数据库完成
    send_my_email(url, email)


def send_my_email(req, rec):
    title = "pingsec code"
    email_from = DEFAULT_FROM_EMAIL
    try:
        # 发送邮件
        reciever = [rec]
        send_mail(title, req, email_from, reciever)
    except Exception as e:
        body = {'code': 500, 'status': 'fail', 'msg': e.__str__()}
        # return HttpResponse(body)
        print(body)
    body = {'code': 200, 'status': 'success', 'msg': '已发送'}
    # return HttpResponse(body)
    print(body)
